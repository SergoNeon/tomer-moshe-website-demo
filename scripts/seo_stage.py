from pathlib import Path
from html import escape
import json,re
root=Path('/root/tomer-moshe-website')

# Correct address everywhere.
repls={
'רח׳ שחם 30, פתח תקווה, ישראל':'גולדנהירש 30, פתח תקווה, ישראל',
'כתובת: רח׳ שחם 30, פתח תקווה, ישראל':'כתובת: גולדנהירש 30, פתח תקווה, ישראל',
'ул. Шахам 30, Петах-Тиква, Израиль':'ул. Голденхирш, 30, Петах-Тиква, Израиль',
'Адрес: ул. Шахам 30, Петах-Тиква, Израиль':'Адрес: ул. Голденхирш, 30, Петах-Тиква, Израиль',
'30 Shaham St., Petah Tikva, Israel':'30 Goldenhirsh St., Petah Tikva, Israel',
'Address: 30 Shaham St., Petah Tikva, Israel':'Address: 30 Goldenhirsh St., Petah Tikva, Israel',
'Goldenhersh 30, Petah Tikva, Israel':'30 Goldenhirsh St., Petah Tikva, Israel',
}
for p in list(root.glob('he/**/*.html'))+list(root.glob('ru/**/*.html'))+list(root.glob('en/**/*.html')):
    s=p.read_text()
    for a,b in repls.items(): s=s.replace(a,b)
    p.write_text(s)

practices={
'he':[
('מקרקעין','עסקאות מכר ורכישה, בדיקות זכויות, רישום, מיסוי מקרקעין, שכירות ועסקאות מול קבלנים.'),
('התחדשות עירונית','ליווי בעלי דירות בפרויקטים של חיזוק, הריסה ובנייה ופינוי־בינוי.'),
('צוואות וירושות','עריכת צוואות, תכנון ירושה, צווי ירושה וניהול עיזבונות.'),
('חברות ומסחרי','ליווי תאגידים, ייעוץ רגולטורי ועסקאות מסחריות.'),
('חוזים','עריכה ובחינה של הסכמים, מכתבי התראה והכנה למחלוקות.'),
('ביטוח לאומי','טיפול בנושאי תאונות עבודה, נכות, מחלות מקצוע וזכויות מול המוסד לביטוח לאומי.'),
('ביטוח ונזיקין','תביעות נזקי גוף, תאונות וסוגיות אחריות.'),
('דיני עבודה','ייעוץ שוטף, ליטיגציה, תאונות עבודה וחבות מעבידים.'),
('הוצאה לפועל','ייצוג חייבים וזוכים, התנגדויות, גביית חובות והסדרים.'),
('חדלות פירעון','הסדרי חוב, הליכי חדלות פירעון, פירוקים וכינוסים.')],
'ru':[
('Недвижимость','Купля-продажа, проверка прав, регистрация, налогообложение недвижимости, аренда и сделки с застройщиками.'),
('Городское обновление','Сопровождение собственников в проектах укрепления, сноса и нового строительства, а также pinui-binui.'),
('Завещания и наследство','Завещания, наследственное планирование, наследственные приказы и управление наследством.'),
('Корпоративное и коммерческое право','Сопровождение компаний, регуляторные вопросы и коммерческие сделки.'),
('Договоры','Подготовка и проверка договоров, претензионные письма и подготовка к спорам.'),
('Битуах Леуми','Вопросы производственных травм, инвалидности, профессиональных заболеваний и социальных прав.'),
('Страхование и деликты','Телесные повреждения, несчастные случаи и вопросы ответственности.'),
('Трудовое право','Текущее консультирование, трудовые споры, производственные травмы и ответственность работодателя.'),
('Исполнительное производство','Представительство должников и взыскателей, возражения, взыскание и соглашения.'),
('Несостоятельность','Урегулирование долгов, процедуры несостоятельности, ликвидация и управление активами.')],
'en':[
('Real estate','Sale and purchase transactions, title checks, registration, real-estate taxation, leases and developer transactions.'),
('Urban renewal','Representation of owners in strengthening, demolition/rebuild and pinui-binui projects.'),
('Wills and estates','Wills, inheritance planning, probate orders and estate administration.'),
('Corporate and commercial','Corporate support, regulatory advice and commercial transactions.'),
('Contracts','Drafting and reviewing agreements, demand letters and dispute preparation.'),
('National Insurance','Work injuries, disability, occupational disease and rights before the National Insurance Institute.'),
('Insurance and torts','Personal injury, accidents and liability matters.'),
('Employment law','Ongoing advice, employment disputes, work accidents and employer liability.'),
('Enforcement proceedings','Representation of debtors and creditors, objections, collection and settlements.'),
('Insolvency','Debt arrangements, insolvency proceedings, liquidation and receivership.')]
}
for lang in ('he','ru','en'):
    p=root/lang/'practice/index.html'; s=p.read_text()
    cards=''.join(f'<article class="detail-card"><span class="detail-dot">◆</span><h3>{escape(t)}</h3><p>{escape(d)}</p></article>' for t,d in practices[lang])
    s=re.sub(r'<div class="detail-grid">.*?</div></div></div></section>',f'<div class="detail-grid">{cards}</div></div></div></section>',s,flags=re.S)
    p.write_text(s)

articles={
'real-estate-deal':{
'he':('עסקת יד שנייה: מה בודקים לפני חתימה?','עסקת מכר או רכישה של דירה דורשת בדיקות משפטיות, תכנוניות וכלכליות לפני התחייבות.',[
('בדיקת הזכויות בנכס','יש לברר מי רשום כבעל הזכויות, האם קיימים שעבודים, עיקולים, הערות או התחייבויות קודמות ומהו מקור הרישום.'),
('בדיקות תכנון ומצב הנכס','כדאי לבחון התאמה בין המצב בפועל לבין היתרים ותוכניות, שימושים מותרים וסוגיות של חריגות בנייה.'),
('תכנון תשלומים ומסים','לפני חתימה יש להבין את מבנה התשלומים, יתרת משכנתה קיימת, מסים והיטלים אפשריים והוצאות נלוות.')]),
'ru':('Вторичный рынок: что проверить до подписания сделки?','Покупка или продажа квартиры требует юридической, регистрационной и финансовой проверки до принятия обязательств.',[
('Права на объект','Проверяют собственника, записи в реестре, залоги, аресты, предупреждающие отметки и иные ограничения.'),
('Планирование и фактическое состояние','Важно сопоставить объект с разрешениями и планами, проверить назначение и возможные строительные отклонения.'),
('Платежи и налоги','До подписания нужно понимать график платежей, остаток ипотеки, возможные налоги, сборы и сопутствующие расходы.')]),
'en':('Second-hand property: what should be checked before signing?','A residential sale or purchase should be reviewed legally, registrationally and financially before binding commitments are made.',[
('Title and registered rights','Review ownership, liens, attachments, cautionary notes and other restrictions affecting the property.'),
('Planning and physical status','Compare the actual property with permits and planning records, permitted use and possible building irregularities.'),
('Payments and taxes','Understand the payment schedule, existing mortgage payoff, potential taxes, levies and related transaction costs.')])},
'contractor-apartment':{
'he':('רכישת דירה מקבלן: האותיות הקטנות שחשוב לקרוא','חוזה קבלן מנוסח בדרך כלל על ידי הקבלן ולכן חשוב לבחון את מנגנוני ההגנה של הרוכש לפני חתימה.',[
('מועד המסירה','יש להבין את מועד המסירה, מנגנון הדחייה והמשמעות הכלכלית של איחור במסירה.'),
('שינויים ותוספות','שדרוגים ושינויים יכולים להגדיל את העלות. מומלץ להבין מראש את המחירון, לוחות הזמנים וההשפעה על המסירה.'),
('תשלומים והוצאות','יש לבדוק אילו מסים, אגרות, הוצאות פיתוח ותשלומים נוספים מוטלים על כל צד לפי הדין וההסכם.')]),
'ru':('Покупка квартиры у застройщика: что читать в мелком шрифте','Договор обычно готовит застройщик, поэтому до подписания важно отдельно проверить механизмы защиты покупателя.',[
('Срок передачи','Нужно понять дату передачи, допустимые переносы и финансовые последствия задержки.'),
('Изменения и улучшения','Дополнительные работы могут существенно увеличить цену. Стоит заранее получить порядок цен и сроки.'),
('Платежи и расходы','Проверяют, какие налоги, сборы, расходы на развитие и иные платежи возлагаются на каждую сторону.')]),
'en':('Buying from a developer: the clauses worth reading closely','Developer agreements are generally drafted by the developer, so buyer protections should be reviewed separately before signing.',[
('Delivery date','Understand the handover date, extension mechanisms and the financial consequences of delay.'),
('Changes and upgrades','Upgrades can materially increase cost. Clarify pricing, deadlines and any effect on delivery before signing.'),
('Taxes and expenses','Check which taxes, fees, development charges and other costs are allocated to each party.')])},
'rental-agreement':{
'he':('הסכם שכירות: למה לא כדאי להסתפק בתבנית מהאינטרנט','הסכם שכירות צריך להתאים לנכס, לצדדים ולסיכונים הספציפיים של העסקה.',[
('בטוחות וערבים','יש להגדיר במדויק אילו בטוחות ניתנות, מתי אפשר לממש אותן ואיך הן מוחזרות בסיום.'),
('מצב הנכס ותיקונים','כדאי לתעד את מצב הדירה ולהגדיר אחריות לתחזוקה, תקלות, נזק וביטוח.'),
('סיום ופינוי','מנגנון יציאה, הארכה, הודעה מוקדמת ופינוי צריכים להיות ברורים מראש כדי לצמצם מחלוקות.')]),
'ru':('Договор аренды: почему интернет-шаблона часто недостаточно','Договор аренды должен учитывать конкретный объект, стороны и реальные риски сделки.',[
('Обеспечение и поручители','Следует ясно определить виды обеспечения, условия их использования и возврата.'),
('Состояние объекта и ремонт','Полезно зафиксировать состояние квартиры и распределить ответственность за обслуживание, поломки и страхование.'),
('Окончание аренды','Условия продления, досрочного выхода, уведомления и освобождения объекта должны быть понятны заранее.')]),
'en':('Lease agreements: why a generic online template may not be enough','A lease should reflect the specific property, the parties and the actual risks of the arrangement.',[
('Security and guarantees','Define what security is provided, when it may be used and how it is returned at the end of the lease.'),
('Condition and repairs','Document the condition of the property and allocate responsibility for maintenance, damage and insurance.'),
('Termination and handover','Renewal, early termination, notice and vacating terms should be clear in advance to reduce disputes.')])},
'urban-renewal':{
'he':('התחדשות עירונית: נקודות מפתח לבעלי דירות','פרויקט התחדשות עירונית הוא עסקה ארוכת טווח שמחברת בין זכויות קנייניות, תכנון, מימון ובטוחות.',[
('הסכם ובטוחות','יש לבחון מה מקבלים בעלי הדירות, מהן אבני הדרך ואילו ערבויות ובטוחות ניתנות לאורך הפרויקט.'),
('פינוי ודיור חלופי','בפרויקט הכולל פינוי חשוב להסדיר דיור חלופי, הובלה, מועדים והוצאות נלוות.'),
('רישום הזכויות','יש לתכנן מראש את רישום הזכויות והדירה החדשה ואת הטיפול בנושאי ירושה או רישום חסר, אם קיימים.')]),
'ru':('Городское обновление: ключевые вопросы для собственников','Проект городского обновления — долгосрочная сделка, объединяющая права на недвижимость, планирование, финансирование и гарантии.',[
('Договор и гарантии','Нужно понимать, что получают собственники, этапы проекта и какие гарантии действуют на каждом этапе.'),
('Выселение и временное жильё','Если требуется освобождение квартиры, заранее регулируют временное жильё, переезд, сроки и расходы.'),
('Регистрация прав','Следует заранее планировать регистрацию новых прав и решать вопросы наследства или неполной регистрации, если они есть.')]),
'en':('Urban renewal: key points for apartment owners','Urban renewal is a long-term transaction combining property rights, planning, finance and project safeguards.',[
('Agreement and safeguards','Understand the consideration to owners, project milestones and the guarantees available throughout the project.'),
('Vacating and alternative housing','Where owners must vacate, alternative housing, moving costs, timing and related expenses should be regulated.'),
('Registration of rights','Plan the registration of the new rights and address inheritance or incomplete registration issues where relevant.')])},
'insolvency-enforcement':{
'he':('חדלות פירעון והוצאה לפועל: איך מתחילים לעשות סדר','כאשר קיימים חובות או הליכי גבייה, הצעד הראשון הוא להבין את התמונה המלאה לפני בחירת מסלול פעולה.',[
('מיפוי החובות וההליכים','מרכזים תיקים, פסקי דין, דרישות תשלום, הכנסות, נכסים והתחייבויות כדי להבין את מצב החוב.'),
('בחירת מסלול','הפתרון עשוי להיות הסדר חוב, טיפול בתיקי הוצאה לפועל או הליך חדלות פירעון — בהתאם לנסיבות.'),
('עמידה במועדים','בהליכי גבייה קיימים מועדים לבקשות, התנגדויות ותגובות. טיפול מוקדם יכול למנוע החמרה מיותרת.')]),
'ru':('Несостоятельность и исполнительное производство: с чего начать','При долгах и взыскании сначала нужно собрать полную картину, а уже затем выбирать юридический маршрут.',[
('Карта долгов и производств','Собирают исполнительные дела, решения, требования, сведения о доходах, активах и обязательствах.'),
('Выбор процедуры','В зависимости от обстоятельств возможны соглашение о долге, работа в исполнительном производстве или процедура несостоятельности.'),
('Сроки','В делах о взыскании действуют сроки для заявлений, возражений и ответов. Раннее реагирование помогает избежать лишнего ухудшения ситуации.')]),
'en':('Insolvency and enforcement: how to start organizing the situation','Where debt and collection proceedings exist, the first step is to map the complete position before choosing a legal route.',[
('Map debts and proceedings','Collect enforcement files, judgments, demands, income information, assets and liabilities to understand the full position.'),
('Choose the appropriate route','Depending on the facts, options may include a debt arrangement, enforcement-file strategy or insolvency proceedings.'),
('Watch deadlines','Collection procedures include deadlines for applications, objections and responses. Early action can prevent avoidable escalation.')])}
}

labels={
'he':dict(brand='תומר משה ושות׳',office='משרד עורכי דין',firm='המשרד',practice='תחומי עיסוק',articles='מאמרים',contact='יצירת קשר',cta='לתיאום שיחה',back='חזרה לכל המאמרים',general='מידע כללי בלבד — אינו מהווה ייעוץ משפטי.',legal='מידע משפטי',privacy='פרטיות והבהרה משפטית',access='נגישות',career='קריירה',contactoffice='יצירת קשר עם המשרד',home='דף הבית'),
'ru':dict(brand='Tomer Moshe & Co.',office='Адвокатское бюро',firm='О фирме',practice='Практики',articles='Статьи',contact='Контакты',cta='Связаться',back='Все статьи',general='Материал носит общий информационный характер и не является юридической консультацией.',legal='Юридическая информация',privacy='Конфиденциальность и отказ от ответственности',access='Доступность',career='Карьера',contactoffice='Связаться с офисом',home='Главная'),
'en':dict(brand='Tomer Moshe & Co.',office='Law Office',firm='Firm',practice='Practice',articles='Articles',contact='Contact',cta='Contact us',back='All articles',general='General information only — not legal advice.',legal='Legal information',privacy='Privacy & Disclaimer',access='Accessibility',career='Careers',contactoffice='Contact the office',home='Home')}

schema_org={"@context":"https://schema.org","@type":"LegalService","@id":"https://www.lawtmo.com/#lawoffice","name":"Tomer Moshe & Co.","url":"https://www.lawtmo.com/","image":"https://www.lawtmo.com/assets/img/tomer-moshe.jpg","email":"office@lawtmo.com","telephone":["+972502692223","+97235209818"],"address":{"@type":"PostalAddress","streetAddress":"גולדנהירש 30","addressLocality":"פתח תקווה","addressCountry":"IL"},"areaServed":{"@type":"Country","name":"Israel"},"availableLanguage":["he","ru","en"]}

def header(lang,slug):
    l=labels[lang]; cur=lambda x: ' aria-current="page"' if x==lang else ''
    return f'''<a class="skip-link" href="#main">Skip</a><header><div class="container nav"><a class="brand" href="../../"><span class="brand-mark">TM</span><span class="brand-copy"><strong>{l['brand']}</strong><span>{l['office']}</span></span></a><nav class="nav-links" aria-label="Main"><a href="../../about/">{l['firm']}</a><a href="../../practice/">{l['practice']}</a><a href="../../articles/">{l['articles']}</a><a href="../../contact/">{l['contact']}</a><a class="nav-cta" href="../../contact/">{l['cta']}</a></nav><div class="lang"><a href="../../../he/articles/{slug}/"{cur('he')}>עברית</a><a href="../../../ru/articles/{slug}/"{cur('ru')}>Русский</a><a href="../../../en/articles/{slug}/"{cur('en')}>English</a></div><button class="menu-btn" aria-expanded="false" aria-label="Menu">☰</button></div></header>'''

def footer(lang):
    l=labels[lang]
    addr={'he':'גולדנהירש 30, פתח תקווה, ישראל','ru':'ул. Голденхирш, 30, Петах-Тиква, Израиль','en':'30 Goldenhirsh St., Petah Tikva, Israel'}[lang]
    return f'''<footer><div class="container footer-grid"><div class="footer-brand"><div class="brand"><span class="brand-mark">TM</span><span class="brand-copy"><strong>{l['brand']}</strong><span>{l['office']}</span></span></div><p>{addr}</p></div><div class="footer-col"><h4>{l['legal']}</h4><a href="../../privacy/">{l['privacy']}</a><a href="../../accessibility/">{l['access']}</a><a href="../../career/">{l['career']}</a></div><div class="footer-col"><h4>{l['contactoffice']}</h4><a href="tel:+972502692223">+972 50-269-2223</a><a href="tel:+97235209818">+972 3-520-9818</a><a href="mailto:office@lawtmo.com">office@lawtmo.com</a></div></div><div class="container footer-bottom"><span>© 2026 {l['brand']}</span><span>{l['general']}</span></div></footer>'''

for slug,data in articles.items():
    for lang in ('he','ru','en'):
        title,desc,sections=data[lang]; direction='rtl' if lang=='he' else 'ltr'; l=labels[lang]
        url=f'https://www.lawtmo.com/{lang}/articles/{slug}/'
        hreflangs=''.join(f'<link rel="alternate" hreflang="{x}" href="https://www.lawtmo.com/{x}/articles/{slug}/">' for x in ('he','ru','en'))+'<link rel="alternate" hreflang="x-default" href="https://www.lawtmo.com/he/articles/'+slug+'/">'
        article_schema={"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"datePublished":"2026-10-05","dateModified":"2026-10-05","inLanguage":lang,"mainEntityOfPage":url,"author":{"@id":"https://www.lawtmo.com/#lawoffice"},"publisher":{"@id":"https://www.lawtmo.com/#lawoffice"}}
        breadcrumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":l['home'],"item":f'https://www.lawtmo.com/{lang}/'},{"@type":"ListItem","position":2,"name":l['articles'],"item":f'https://www.lawtmo.com/{lang}/articles/'},{"@type":"ListItem","position":3,"name":title,"item":url}]}
        sec=''.join(f'<section class="article-section"><h2>{escape(h)}</h2><p>{escape(p)}</p></section>' for h,p in sections)
        html=f'''<!doctype html><html lang="{lang}" dir="{direction}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | {escape(l['brand'])}</title><meta name="description" content="{escape(desc)}"><link rel="canonical" href="{url}">{hreflangs}<meta property="og:type" content="article"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://www.lawtmo.com/assets/img/tomer-moshe.jpg"><meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="../../../assets/styles.css"><script type="application/ld+json">{json.dumps(schema_org,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(article_schema,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(breadcrumb,ensure_ascii=False)}</script></head><body dir="{direction}">{header(lang,slug)}<main id="main"><article><section class="article-hero dark"><div class="container article-hero-inner"><div class="eyebrow">{l['articles']} · 05.10.2026</div><h1>{escape(title)}</h1><p>{escape(desc)}</p><a class="text-link" href="../">← {l['back']}</a></div></section><section class="section"><div class="container article-layout"><div class="article-copy"><p class="lead-paragraph">{escape(desc)}</p>{sec}<div class="article-disclaimer">{l['general']}</div></div><aside class="article-aside"><span>{l['contactoffice']}</span><a href="tel:+972502692223">+972 50-269-2223</a><a href="mailto:office@lawtmo.com">office@lawtmo.com</a><a class="btn btn-primary" href="../../contact/">{l['cta']}</a></aside></div></section></article></main>{footer(lang)}<script src="../../../assets/site.js"></script></body></html>'''
        out=root/lang/'articles'/slug/'index.html'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(html)

# Rebuild article indexes as linked cards.
for lang in ('he','ru','en'):
    p=root/lang/'articles/index.html'; s=p.read_text(); l=labels[lang]
    cards=[]
    for slug,data in articles.items():
        title,desc,_=data[lang]
        read={'he':'לקריאת המאמר','ru':'Читать материал','en':'Read article'}[lang]
        cards.append(f'<a class="article-list-card" href="./{slug}/"><span class="detail-dot">◆</span><h3>{escape(title)}</h3><p>{escape(desc)}</p><span class="read">{read} →</span></a>')
    grid='<div class="article-list-grid">'+''.join(cards)+'</div>'
    s=re.sub(r'<div class="detail-grid">.*?</div></div></div></section>',grid+'</div></div></section>',s,flags=re.S)
    p.write_text(s)

# Inject LegalService schema and social metadata into regular content pages.
for p in list(root.glob('he/**/*.html'))+list(root.glob('ru/**/*.html'))+list(root.glob('en/**/*.html')):
    s=p.read_text()
    if '"@type": "LegalService"' in s or '"@type":"LegalService"' in s: continue
    mtitle=re.search(r'<title>(.*?)</title>',s); mdesc=re.search(r'<meta name="description" content="(.*?)">',s); mcan=re.search(r'<link rel="canonical" href="(.*?)">',s)
    if not (mtitle and mdesc and mcan): continue
    metas=f'<meta property="og:type" content="website"><meta property="og:title" content="{mtitle.group(1)}"><meta property="og:description" content="{mdesc.group(1)}"><meta property="og:url" content="{mcan.group(1)}"><meta property="og:image" content="https://www.lawtmo.com/assets/img/tomer-moshe.jpg"><meta name="twitter:card" content="summary_large_image"><script type="application/ld+json">{json.dumps(schema_org,ensure_ascii=False)}</script>'
    s=s.replace('</head>',metas+'</head>')
    p.write_text(s)

# Sitemap: all public pages including articles.
urls=[]
for lang in ('he','ru','en'):
    for rel in ('','about/','practice/','articles/','contact/','career/','accessibility/','privacy/'):
        urls.append(f'https://www.lawtmo.com/{lang}/{rel}')
    for slug in articles: urls.append(f'https://www.lawtmo.com/{lang}/articles/{slug}/')
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{u}</loc><lastmod>2026-10-05</lastmod></url>\n' for u in urls)+'</urlset>\n'
(root/'sitemap.xml').write_text(sm)
