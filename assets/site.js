const menuButton=document.querySelector(".menu-btn");
const navLinks=document.querySelector(".nav-links");
if(menuButton&&navLinks){menuButton.addEventListener("click",()=>{const open=navLinks.classList.toggle("open");menuButton.setAttribute("aria-expanded",String(open));menuButton.textContent=open?"×":"☰"});navLinks.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{navLinks.classList.remove("open");menuButton.setAttribute("aria-expanded","false");menuButton.textContent="☰"}))}
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add("visible");observer.unobserve(entry.target)}}),{threshold:.12});
document.querySelectorAll(".reveal").forEach(el=>observer.observe(el));
const form=document.querySelector("[data-contact-form]");
if(form){form.addEventListener("submit",e=>{e.preventDefault();const status=form.querySelector(".form-status");const lang=document.documentElement.lang;const messages={he:"הטופס מוכן. חיבור השליחה למייל יופעל בשלב ההשקה.",ru:"Форма готова. Отправка на почту будет подключена на этапе запуска.",en:"The form is ready. Email delivery will be connected at launch."};status.textContent=messages[lang]||messages.en})}
