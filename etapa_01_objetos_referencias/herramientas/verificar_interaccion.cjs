/* Prueba la interacción real del formulario en un DOM simulado, sin navegador. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.resolve(__dirname, '../..');
const web = path.join(root, 'dist');
const dom = new JSDOM(fs.readFileSync(path.join(web, 'index.html'), 'utf8'), {
  runScripts: 'outside-only', url: 'https://example.test/',
});
const w = dom.window, d = w.document;
w.matchMedia = () => ({matches: false});
w.scrollTo = () => {};
const tools = new Map();
d.modelContext = {registerTool: tool => tools.set(tool.name, tool)};
w.eval(fs.readFileSync(path.join(web, 'contenido.js'), 'utf8'));
w.eval(fs.readFileSync(path.join(web, 'guia.js'), 'utf8'));
const data = w.DSA;
function navigate(number, view = 'ejercicios') {
  w.location.hash = `#tema-${number}-${view}`;
  w.dispatchEvent(new w.HashChangeEvent('hashchange'));
}
function getForm(id) {return d.querySelector(`form[data-exercise="${id}"]`);}
function submit(form) {form.dispatchEvent(new w.Event('submit', {bubbles: true, cancelable: true}));}
function set(control, value) {control.value = value; control.dispatchEvent(new w.Event('input', {bubbles: true}));}
function feedback(form) {return form.closest('.exercise').querySelector('.feedback');}
function fill(form, c, wrong = false) {
  const answers = c.expected.trimEnd().split('\n');
  [...form.querySelectorAll('select')].forEach((select, i) => {
    const answer = wrong && i === 0 ? c.options[i].find(value => value !== answers[i]) : answers[i];
    set(select, answer);
  });
  form.querySelectorAll('textarea').forEach(input => set(input, 'Mi explicación: sigo las referencias y distingo el objeto que cambia.'));
}
let checked = 0;
for (const unit of data.units) {
  navigate(unit.number);
  for (const exercise of unit.exercises) {
    for (const c of exercise.cases) {
      d.querySelector(`button[data-exercise="${exercise.id}"][data-case="${c.key}"]`).click();
      let form = getForm(exercise.id);
      assert.equal(feedback(form), null, 'La respuesta debe empezar oculta');
      submit(form);
      assert.equal(feedback(form), null, 'Un caso vacío no revela soluciones');
      assert.match(form.querySelector('.form-status').textContent, /Completa todas/);
      fill(form, c);
      set(form.querySelector('textarea'), '   \n  ');
      submit(form);
      assert.equal(feedback(form), null, 'Los espacios no cuentan como respuesta');
      fill(form, c, true);
      submit(form);
      assert(feedback(form));
      assert.match(feedback(form).textContent, /Revisa estas salidas/);
      assert.equal(feedback(form).querySelectorAll('.incorrect').length, 1);
      fill(form, c);
      assert.equal(feedback(form), null, 'Editar vuelve a ocultar la solución');
      submit(form);
      assert.match(feedback(form).textContent, /Tus salidas coinciden/);
      assert.equal(feedback(form).querySelectorAll('.incorrect').length, 0);
      assert.equal(feedback(form).querySelectorAll('.correct').length, c.options.length);
      checked++;
    }
    // Back to the initial case: selected outputs and text survive the tab switch.
    d.querySelector(`button[data-exercise="${exercise.id}"][data-case="inicial"]`).click();
    const form = getForm(exercise.id);
    assert.equal(form.querySelector('select').value, exercise.cases[0].expected.trimEnd().split('\n')[0]);
    assert(form.querySelector('textarea').value);
    assert(feedback(form));
  }
  const lab = data.labs.find(item => item.section === unit.number);
  if (lab) {
    d.querySelector('[data-view="laboratorio"]').click();
    const form = getForm(lab.id), c = lab.cases[0];
    assert.equal(form.querySelectorAll('textarea').length, 3);
    submit(form); assert.equal(feedback(form), null);
    fill(form, c);
    set(form.querySelectorAll('textarea')[2], '');
    submit(form); assert.equal(feedback(form), null, 'Se exige la comprobación de la propuesta');
    fill(form, c); submit(form);
    assert(feedback(form).querySelector('.lab-review'));
    checked++;
  }
}
navigate('1.1');
let form = getForm('E01');
assert.equal(form.querySelector('select').value, 'hola', 'Navegar conserva la respuesta');
assert.equal(form.querySelectorAll('select').length, 2, 'E01 tiene dos salidas');
assert.equal(form.querySelectorAll('textarea').length, 1, 'E01 tiene una explicación');
// A missing output hides already revealed answers, even if the text is filled.
set(form.querySelector('select'), '');submit(form);assert.equal(feedback(form), null);
const verifyTool = tools.get('verify_completed_exercise');
assert(verifyTool && tools.has('read_learning_context'));
assert.equal(verifyTool.execute({exerciseId: 'E01'}).complete, false);
assert.throws(() => verifyTool.execute({exerciseId: 'E99'}), /Abre primero/);
assert.throws(() => verifyTool.execute({exerciseId: '<script>'}), /inválido/);
fill(form,data.units[0].exercises[0].cases[0]);
assert.equal(verifyTool.execute({exerciseId:'E01'}).correctOutputs, 2);
assert(feedback(form), 'El acceso opcional usa el mismo formulario visible');
// Text containing HTML is preserved as text after changing tabs, never executed.
set(form.querySelector('textarea'), '<img src=x onerror="window.injected=true">');
d.querySelector('[data-exercise="E01"][data-case="variacion"]').click();
d.querySelector('[data-exercise="E01"][data-case="inicial"]').click();
form=getForm('E01');assert.equal(w.injected,undefined);assert.match(form.querySelector('textarea').value,/<img/);
submit(form);form.closest('.exercise').querySelector('.retry').click();
form=getForm('E01');assert.equal(form.querySelector('select').value,'');assert.equal(form.querySelector('textarea').value,'');assert.equal(feedback(form),null);
// Keyboard tabs and accessible control relationships.
const initialTab=d.querySelector('[data-exercise="E01"][data-case="inicial"]');
initialTab.dispatchEvent(new w.KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}));
assert.equal(d.querySelector('[data-exercise="E01"][data-case="variacion"]').getAttribute('aria-selected'),'true');
for(const tab of d.querySelectorAll('[aria-controls]')) assert(d.getElementById(tab.getAttribute('aria-controls')), 'Cada pestaña tiene un panel');
for(const input of d.querySelectorAll('select,textarea')) assert(d.querySelector(`label[for="${input.id}"]`),'Cada campo tiene etiqueta');
console.log(`Correcto: ${checked} casos, bloqueo de respuestas incompletas, corrección, pestañas, navegación y controles accesibles en DOM simulado.`);
dom.window.close();
