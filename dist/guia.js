/* Guía estática. No ejecuta Python ni califica automáticamente las explicaciones. */
(() => {
  'use strict';
  const data = window.DSA;
  if (!data) return;
  const main = document.getElementById('contenido');
  const nav = document.getElementById('temas');
  const drafts = new Map();
  const selectedCases = new Map();
  let currentUnit = data.units[0];
  let currentView = 'lectura';
  const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const rich = value => String(value).split(/(`[^`]+`)/g).map(part => part.startsWith('`') && part.endsWith('`') ? `<code>${esc(part.slice(1, -1))}</code>` : esc(part)).join('');
  const paragraphs = values => values.map(value => `<p>${rich(value)}</p>`).join('');
  const code = source => `<pre class="python"><code>${esc(source.trimEnd())}</code></pre>`;
  const table = value => `<div class="table-scroll"><table><thead><tr>${value.headers.map(h => `<th scope="col">${rich(h)}</th>`).join('')}</tr></thead><tbody>${value.rows.map(row => `<tr>${row.map(cell => `<td>${rich(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  const stateKey = (exercise, c) => `${exercise.id}:${c.key}`;
  function draft(exercise, c) {
    const key = stateKey(exercise, c);
    if (!drafts.has(key)) drafts.set(key, {outputs: c.options.map(() => ''), written: c.prompts.map(() => ''), verified: false});
    return drafts.get(key);
  }
  function currentCase(exercise) {
    return exercise.cases.find(c => c.key === selectedCases.get(exercise.id)) || exercise.cases[0];
  }
  function findExercise(id) {
    return currentUnit.exercises.find(e => e.id === id) || data.labs.find(lab => lab.id === id && lab.section === currentUnit.number);
  }
  function complete(state, c) {
    return c.options.every((opts, i) => opts.includes(state.outputs[i])) && c.prompts.every((_, i) => !!state.written[i]?.trim());
  }
  function evaluate(state, c) {
    if (!complete(state, c)) return {complete: false};
    const expected = c.expected.trimEnd().split('\n');
    return {complete: true, correct: expected.map((value, i) => state.outputs[i] === value)};
  }
  function feedback(exercise, c, state) {
    if (!state.verified || !complete(state, c)) return '';
    const result = evaluate(state, c);
    const count = result.correct.filter(Boolean).length;
    const expected = c.expected.trimEnd().split('\n');
    return `<section class="feedback" aria-label="Revisión de ${exercise.id}">
      <h3>${count === expected.length ? 'Tus salidas coinciden' : 'Revisa estas salidas'}</h3>
      <p class="score">${count} de ${expected.length} líneas de salida correctas.</p>
      <div class="output-review">${expected.map((value, i) => `<div class="review-row ${result.correct[i] ? 'correct' : 'incorrect'}"><span>Línea ${i + 1} · ${result.correct[i] ? 'Correcta' : 'Por revisar'}</span><p>Elegiste: <code>${esc(state.outputs[i])}</code></p>${result.correct[i] ? '' : `<p>Salida correcta: <code>${esc(value)}</code></p>`}</div>`).join('')}</div>
      <h3>Compara tu razonamiento</h3><p>${rich(c.answer)}</p>
      <p class="muted">La explicación escrita no se califica automáticamente. Compárala con el razonamiento y revisa qué objeto cambia o qué referencia se mueve.</p>
      ${c.review ? `<div class="lab-review">${paragraphs(c.review)}<h3>Una propuesta de solución</h3>${code(c.solution.code)}<p>${rich(c.solution.explanation)}</p><p class="small-label">Salida de la propuesta</p><pre class="output"><code>${esc(c.solution.expected.trimEnd())}</code></pre></div>` : ''}
      <button class="secondary retry" type="button" data-exercise="${exercise.id}">Volver a intentar este caso</button>
    </section>`;
  }
  function exerciseHTML(exercise) {
    const c = currentCase(exercise), state = draft(exercise, c);
    const panelId = `panel-${exercise.id}-${c.key}`;
    const tabs = exercise.cases.length > 1 ? `<div class="tabs case-tabs" role="tablist" aria-label="Casos de ${exercise.id}">${exercise.cases.map(item => `<button type="button" role="tab" id="tab-${exercise.id}-${item.key}" aria-controls="panel-${exercise.id}-${item.key}" aria-selected="${item.key === c.key}" tabindex="${item.key === c.key ? 0 : -1}" data-case="${item.key}" data-exercise="${exercise.id}">${item.label}</button>`).join('')}</div>` : '';
    const inputs = c.options.map((opts, i) => `<div class="output-field"><label for="${exercise.id}-${c.key}-out-${i}">Línea ${i + 1} de salida</label><select id="${exercise.id}-${c.key}-out-${i}" name="output-${i}" data-kind="outputs" data-index="${i}" required><option value="">Elige la salida…</option>${opts.map(option => `<option value="${esc(option)}" ${state.outputs[i] === option ? 'selected' : ''}>${esc(option)}</option>`).join('')}</select></div>`).join('');
    const writing = c.prompts.map((prompt, i) => `<div class="writing-field"><label for="${exercise.id}-${c.key}-why-${i}">${rich(prompt)}</label><textarea id="${exercise.id}-${c.key}-why-${i}" name="reason-${i}" data-kind="written" data-index="${i}" rows="${c.prompts.length > 1 && i === 1 ? 7 : 4}" required placeholder="Escribe tu respuesta con tus palabras…">${esc(state.written[i])}</textarea></div>`).join('');
    return `<section class="exercise" id="${exercise.id.toLowerCase()}" data-exercise="${exercise.id}"><h2><span class="exercise-id">${exercise.id}</span><span class="exercise-title">${esc(exercise.title)}</span></h2>
      ${exercise.goal ? `<p>${rich(exercise.goal)}</p>` : ''}${tabs}
      <div id="${panelId}" ${tabs ? `role="tabpanel" aria-labelledby="tab-${exercise.id}-${c.key}"` : ''}>
      ${c.change ? `<p class="change-note"><strong>Qué cambia:</strong> ${rich(c.change)}</p>` : ''}
      ${code(c.code)}
      ${exercise.tasks ? `<h3>Trabajo de la práctica</h3><ol>${exercise.tasks.map(task => `<li>${rich(task)}</li>`).join('')}</ol>` : ''}
      <form novalidate data-exercise="${exercise.id}" data-case="${c.key}">
        <fieldset><legend>1. Anticipa la salida</legend><p class="field-help">Elige qué aparece en cada línea de la consola. Respeta corchetes, comillas y mayúsculas.</p><div class="output-fields">${inputs}</div></fieldset>
        <fieldset><legend>2. Explica por qué</legend>${writing}</fieldset>
        <div class="form-actions"><button class="primary" type="submit">Verificar mis respuestas</button><p>Completa todas las respuestas para consultar la solución.</p></div>
        <p class="form-status" aria-live="polite" role="status"></p>
      </form><div class="feedback-slot">${feedback(exercise, c, state)}</div></div>${exercise.cases.filter(item=>item.key!==c.key).map(item=>`<div role="tabpanel" id="panel-${exercise.id}-${item.key}" aria-labelledby="tab-${exercise.id}-${item.key}" hidden></div>`).join('')}</section>`;
  }
  function analogyHTML() {
    const a = data.analogy;
    return `<section class="analogy"><p class="small-label">Una analogía para seguir las referencias</p><h2>${esc(a.title)}</h2>${paragraphs([a.intro, a.labels])}${table(a.table)}<div class="card-comparison"><div><h3><code>x = x</code></h3><p>${rich(a.same)}</p></div><div><h3><code>x = x + 1</code></h3><p>${rich(a.other)}</p></div></div>${code(a.code)}<p>Salida: <code>True</code> y después <code>False</code>.</p><p>${rich(a.conclusion)}</p></section>`;
  }
  function readingHTML(unit) {
    const example = unit.example;
    return `<p class="opening-question">${rich(unit.question)}</p>${paragraphs(unit.concepts)}${unit.table ? table(unit.table) : ''}
      ${unit.number === '1.1' ? analogyHTML() : ''}
      <section class="worked-example"><p class="small-label">Ejemplo resuelto</p><h2>${example.id.toUpperCase()} | ${esc(example.title)}</h2>${code(example.code)}<p class="small-label">Salida</p><pre class="output"><code>${esc(example.expected.trimEnd())}</code></pre><p>${rich(example.explanation)}</p><figure><img src="diagramas/${unit.diagram}.svg" alt="Referencias del ejemplo ${example.id.toUpperCase()}: ${esc(example.explanation.replaceAll('`',''))}"><figcaption>Las flechas representan referencias; los folios distinguen objetos.</figcaption></figure></section>
      <aside class="notice"><strong>Observa</strong><p>${rich(unit.pitfall)}</p></aside>
      <button class="primary go-practice" type="button">Practicar con ${unit.exercises.map(e => e.id).join(' y ')}</button>`;
  }
  function reviewHTML() {
    return `<article class="lesson"><p class="eyebrow">Cierre de la etapa 1</p><h1>Explica lo que aprendiste</h1><p>Vuelve a un ejercicio que al principio te haya costado. Sin mirar la solución, explica qué objetos hay, qué referencias comparten y qué instrucción produce el cambio.</p><ul><li>¿Distingues un objeto mutable de una variable que pasa a señalar otro?</li><li>¿Puedes justificar cuándo usar <code>==</code> y cuándo usar <code>is</code>?</li><li>¿Sabes qué cambia dentro y fuera de una función?</li><li>¿Puedes elegir qué partes copiar para obtener el comportamiento que necesitas?</li></ul><p>Si algo sigue sin quedar claro, vuelve al tema correspondiente y sigue cada flecha. Puedes dibujarlo en tu cuaderno.</p><h2>Glosario</h2>${table({headers:['Término','Qué significa'],rows:[['Objeto','Dato con tipo, valor e identidad.'],['Referencia','Relación que permite llegar a un objeto desde un nombre o un contenedor.'],['Identidad','Lo que distingue a un objeto concreto; permanece mientras existe.'],['Alias','Otro nombre o referencia que señala el mismo objeto.'],['Mutación','Cambio del contenido de un objeto existente.'],['Asignación','Indicar qué objeto señala un nombre; puede ser el mismo que antes u otro.'],['Copia superficial','Otra lista o diccionario exterior, con referencias a los mismos elementos.'],['Copia profunda','Copia también los contenedores interiores de nuestros ejemplos; puede conservar referencias compartidas dentro de la copia.']]})}<h2>Fuentes para ampliar</h2><ul class="sources">${data.sources.map(([title,url,note])=>`<li><a href="${esc(url)}" target="_blank" rel="noopener">${esc(title)}</a><p>${rich(note)}</p></li>`).join('')}</ul><p>Las fuentes son de consulta. Puedes aprender con esta guía y comprobar los programas localmente, sin servicios en línea.</p></article>`;
  }
  function render() {
    const closure = location.hash === '#cierre';
    nav.innerHTML = data.units.map(unit => `<a href="#tema-${unit.number}" ${!closure && unit.number === currentUnit.number ? 'aria-current="page"' : ''}><span>${unit.number}</span> ${esc(unit.title)}</a>`).join('') + `<a href="#cierre" ${closure ? 'aria-current="page"' : ''}>Cierre, glosario y fuentes</a>`;
    if (closure) { main.innerHTML = reviewHTML(); return; }
    const lab = data.labs.find(l => l.section === currentUnit.number);
    const views = [['lectura','Lectura'],['ejercicios','Ejercicios'],...(lab ? [['laboratorio',lab.id + ' · Laboratorio']] : [])];
    let content = readingHTML(currentUnit);
    if (currentView === 'ejercicios') content = `<p class="practice-intro">Resuelve cada caso desde el inicio. Puedes apoyar tu explicación con un dibujo en tu cuaderno. La pestaña <strong>Variación</strong> propone un cambio para volver a pensar el ejemplo.</p>${currentUnit.exercises.map(exerciseHTML).join('')}<aside class="checkpoint"><h2>Antes de avanzar</h2><p>${rich(currentUnit.checkpoint)}</p></aside>`;
    if (currentView === 'laboratorio' && lab) content = `<p>Trabaja en Python desde tu computadora. Primero predice; después ejecuta y registra lo que ocurrió. La revisión incluye una propuesta de solución cuando completes todas tus respuestas.</p>${exerciseHTML(lab)}`;
    const index = data.units.indexOf(currentUnit);
    main.innerHTML = `<article class="lesson"><p class="eyebrow">Etapa 1 · Tema ${currentUnit.number}</p><h1>${esc(currentUnit.title)}</h1><p class="goal">${rich(currentUnit.goal)}</p><div class="tabs view-tabs" role="tablist" aria-label="Contenido del tema">${views.map(([key,label])=>`<button type="button" role="tab" id="view-${key}" aria-controls="view-panel-${key}" aria-selected="${currentView===key}" tabindex="${currentView===key ? 0 : -1}" data-view="${key}">${label}</button>`).join('')}</div><div class="view-content" role="tabpanel" id="view-panel-${currentView}" aria-labelledby="view-${currentView}">${content}</div>${views.filter(([key])=>key!==currentView).map(([key])=>`<div role="tabpanel" id="view-panel-${key}" aria-labelledby="view-${key}" hidden></div>`).join('')}<nav class="lesson-navigation" aria-label="Avanzar por la guía">${index ? `<a href="#tema-${data.units[index-1].number}">Tema anterior</a>` : '<span></span>'}<a href="${index < data.units.length - 1 ? '#tema-'+data.units[index+1].number : '#cierre'}">${index < data.units.length - 1 ? 'Siguiente tema' : 'Ir al cierre'}</a></nav></article>`;
  }
  function showView(view, focus = false) {
    currentView = view; render();
    if (focus) document.getElementById(`view-${view}`)?.focus();
  }
  function syncInput(target) {
    const form = target.closest('form');
    if (!form || !target.dataset.kind) return;
    const exercise = findExercise(form.dataset.exercise);
    const c = exercise.cases.find(item => item.key === form.dataset.case);
    const state = draft(exercise, c);
    state[target.dataset.kind][Number(target.dataset.index)] = target.value;
    state.verified = false;
    target.removeAttribute('aria-invalid');
    form.querySelector('.form-status').textContent = '';
    form.closest('.exercise').querySelector('.feedback-slot').innerHTML = '';
  }
  function verify(form) {
    const exercise = findExercise(form.dataset.exercise);
    const c = exercise.cases.find(item => item.key === form.dataset.case);
    const state = draft(exercise, c);
    // Read the actual controls as well, including values set by browser autofill.
    form.querySelectorAll('[data-kind]').forEach(input => { state[input.dataset.kind][Number(input.dataset.index)] = input.value; });
    const result = evaluate(state, c);
    const status = form.querySelector('.form-status');
    if (!result.complete) {
      state.verified = false;
      form.closest('.exercise').querySelector('.feedback-slot').innerHTML = '';
      status.textContent = 'Completa todas las salidas y respuestas escritas. No se pueden mostrar las respuestas correctas mientras falte alguna respuesta.';
      let first = null;
      form.querySelectorAll('[data-kind]').forEach(input => {
        const missing = !input.value.trim();
        if (missing) { input.setAttribute('aria-invalid','true'); first ||= input; }
      });
      first?.focus();
      return {complete:false};
    }
    state.verified = true;
    status.textContent = 'Revisión disponible debajo. Compara las salidas y tu explicación.';
    form.closest('.exercise').querySelector('.feedback-slot').innerHTML = feedback(exercise,c,state);
    return {complete:true, correctOutputs:result.correct.filter(Boolean).length,totalOutputs:result.correct.length};
  }
  main.addEventListener('input', event => syncInput(event.target));
  main.addEventListener('change', event => syncInput(event.target));
  main.addEventListener('submit', event => {event.preventDefault();verify(event.target);});
  main.addEventListener('click', event => {
    const button = event.target.closest('button'); if (!button) return;
    if (button.dataset.view) return showView(button.dataset.view,true);
    if (button.classList.contains('go-practice')) return showView('ejercicios',true);
    if (button.dataset.case) {
      selectedCases.set(button.dataset.exercise,button.dataset.case);
      const exercise = findExercise(button.dataset.exercise);
      button.closest('.exercise').outerHTML = exerciseHTML(exercise);
      document.getElementById(`tab-${exercise.id}-${button.dataset.case}`)?.focus();
    }
    if (button.classList.contains('retry')) {
      const exercise = findExercise(button.dataset.exercise), c = currentCase(exercise);
      drafts.delete(stateKey(exercise,c));
      button.closest('.exercise').outerHTML = exerciseHTML(exercise);
      document.getElementById(`${exercise.id}-${c.key}-out-0`)?.focus();
    }
  });
  main.addEventListener('keydown', event => {
    if (!event.target.matches('[role="tab"]')) return;
    const tabs = [...event.target.closest('[role="tablist"]').querySelectorAll('[role="tab"]')];
    let index = tabs.indexOf(event.target);
    if(event.key==='ArrowRight') index=(index+1)%tabs.length;
    else if(event.key==='ArrowLeft') index=(index-1+tabs.length)%tabs.length;
    else if(event.key==='Home') index=0;
    else if(event.key==='End') index=tabs.length-1;
    else return;
    event.preventDefault();tabs[index].click();
  });
  function navigate() {
    const match = location.hash.match(/^#tema-(1\.(?:10|[1-9]))(?:-(lectura|ejercicios|laboratorio))?$/);
    if(match) { currentUnit=data.units.find(unit=>unit.number===match[1]);currentView=match[2]||'lectura'; }
    if(currentView==='laboratorio' && !data.labs.some(l=>l.section===currentUnit.number)) currentView='lectura';
    render();
  }
  window.addEventListener('hashchange',()=>{navigate();main.focus({preventScroll:true});window.scrollTo({top:0});});
  if(window.matchMedia('(max-width:680px)').matches) document.querySelector('.sidebar details').open=false;
  navigate();
  // Optional browser integration: it uses the same completion rule as the form.
  const context = document.modelContext;
  if(context?.registerTool) {
    const lifecycle = new AbortController();
    const registry = [{name:'read_learning_context',title:'Consultar el tema actual',description:'Devuelve el tema y los casos visibles, sin revelar soluciones pendientes.',inputSchema:{type:'object',properties:{},additionalProperties:false},annotations:{readOnlyHint:true},execute:()=>({topic:currentUnit.number,title:currentUnit.title,view:currentView,exercises:currentUnit.exercises.map(e=>({id:e.id,case:currentCase(e).key,completed:complete(draft(e,currentCase(e)),currentCase(e))}))})},
      {name:'verify_completed_exercise',title:'Verificar un ejercicio respondido',description:'Verifica respuestas ya escritas en el formulario visible. Rechaza formularios incompletos y no rellena respuestas.',inputSchema:{type:'object',properties:{exerciseId:{type:'string'}},required:['exerciseId'],additionalProperties:false},annotations:{readOnlyHint:false},execute:input=>{
        if(!input||typeof input.exerciseId!=='string'||!/^E\d{2}$|^P\d{2}$/.test(input.exerciseId)) throw new Error('Identificador de ejercicio inválido.');
        const forms=[...main.querySelectorAll('form')];const form=forms.find(f=>f.dataset.exercise===input.exerciseId);
        if(!form) throw new Error('Abre primero el ejercicio en la interfaz.');
        return verify(form);
      }}];
    for(const tool of registry) {try{Promise.resolve(context.registerTool(tool,{signal:lifecycle.signal})).catch(()=>{});}catch{}}
    window.addEventListener('pagehide',()=>lifecycle.abort(),{once:true});
  }
})();
