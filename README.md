# AI Insight Hub

Actúa como un desarrollador Frontend experto y diseñador UI/UX. Quiero construir un portfolio profesional freelance de una sola página (Single Page Application) optimizado para alta conversión.

### 1. Stack Tecnológico y Configuración (CRÍTICO PARA GITHUB PAGES)
- Usa React, Vite, Tailwind CSS y componentes de shadcn/ui.
- Usa iconos de lucide-react.
- REQUISITO ESTRICTO: Si implementas enrutamiento, debes usar `HashRouter` en lugar de `BrowserRouter` para evitar errores 404 al recargar la página en GitHub Pages.
- Asegúrate de que las rutas a los assets sean relativas.
- El código final debe estar totalmente libre de errores, listo para exportarse y desplegarse como un sitio estático.

### 2. Diseño Visual y UI/UX
- Estilo: Minimalista, moderno, elegante y muy centrado en la conversión y usabilidad.
- Paleta de colores: Tema oscuro (Dark Mode) profesional. Fondos en grises muy oscuros casi negros, texto principal en blanco/gris claro, y un color de acento vibrante (como azul eléctrico o cian) para los botones y elementos interactivos.
- Tipografía: Sans-serif limpia y profesional (como Inter, Roboto o similar).
- Interacciones: Scroll suave (smooth scrolling) en los enlaces de navegación, animaciones sutiles de "fade-in" al hacer scroll, y efectos hover elegantes en botones y tarjetas.

### 3. Estructura y Contenido (Copywriting Persuasivo)
Desarrolla la página con la siguiente estructura de secciones en orden descendente. Presta especial atención al diseño de cada bloque e incluye los siguientes textos literales:

1. HERO SECTION (Inicio):
- Titular principal (H1): Inteligencia Artificial y Datos: De la Complejidad a los Resultados Reales.
- Subtítulo: Soy Iván Palomares, PhD en IA. Ayudo a empresas a dominar el Machine Learning y la IA Generativa mediante formación corporativa de alto impacto y creación de contenido técnico especializado (Tech Writing).
- Call to Action (Botón principal): "Hablemos de tu proyecto" (debe hacer scroll hacia la sección de contacto).

2. SERVICIOS / SOLUCIONES QUE OFREZCO:
- Texto introductorio: Con más de 15 años de experiencia tecnológica, trabajo en la intersección entre la tecnología profunda y el valor empresarial. Estas son mis áreas de especialidad:
- 3 Tarjetas (Cards) de servicios visualmente destacadas:
  - Tarjeta 1: Formación Corporativa Global. Diseño e imparto programas a medida sobre Python, Machine Learning, LLMs y automatización (n8n) para capacitar a equipos técnicos y de negocio, presencial u online.
  - Tarjeta 2: Tech Writing y Divulgación. Redacción experta de artículos y documentación técnica sobre IA. Autor en plataformas de referencia mundial como Machine Learning Mastery y KDnuggets.
  - Tarjeta 3: Consultoría en IA y Datos. Asesoramiento estratégico para integrar soluciones basadas en IA y automatización de flujos que resuelvan problemas reales de negocio.

3. EXPERIENCIA DESTACADA / CASOS DE ÉXITO:
- Crea una línea de tiempo (timeline) o cuadrícula de hitos destacando esta trayectoria:
  - Hito 1: Lead Tech Writer. Autor principal de contenidos avanzados (NLP, LLMs) para audiencias globales en Machine Learning Mastery, KDnuggets y DataCamp.
  - Hito 2: Instructor y Profesor Internacional. Diseño e impartición de formaciones B2B para ejecutivos y equipos técnicos en instituciones como EU Business School, EAE y empresas multinacionales.
  - Hito 3: Liderazgo Corporativo en IA. Experiencia dirigiendo estrategias de IA Generativa y MLOps como Ex-Head of AI en Loyal Guru y Senior Manager en Capgemini.

4. SOBRE MÍ:
- Título de la sección: La IA no es magia, es ingeniería.
- Texto: Soy Doctor (PhD) en Inteligencia Artificial. Durante la actual euforia generativa, aporto el rigor de mi perfil académico (ex-profesor universitario e investigador internacional) combinado con mi experiencia en consultoría corporativa. Trabajo con fluidez en español e inglés, convencido de que el éxito de cualquier modelo predictivo o sistema generativo reside en una base absoluta: la calidad de los datos.

5. SECCIÓN DE CONTACTO Y FOOTER (DISEÑADO PARA SITIOS ESTÁTICOS):
- Texto introductorio: "¿Necesitas una voz experta para tus publicaciones técnicas o un formador que capacite a tu equipo? Hablemos."
- Crea un formulario de contacto funcional sin necesidad de backend, utilizando FormSubmit.
- El formulario HTML (o componente React) debe apuntar mediante método POST a: `https://formsubmit.co/gakudo.learn@gmail.com`
- Campos visuales obligatorios con buen espaciado y diseño:
  - Nombre completo (input type text, name="name")
  - Email (input type email, name="email")
  - Tu consulta (textarea, name="message")
- Campos ocultos (hidden) requeridos para el funcionamiento:
  - name="_subject", value="Nuevo contacto desde la web freelance"
  - name="_captcha", value="false"
- Botón de envío estilizado ("Enviar mensaje").
- En el Footer (pie de página): Incluye el copyright del año actual y enlaces a mi LinkedIn (www.linkedin.com/in/ivanpc) y GitHub (https://github.com/ivanpc), usando iconos de lucide-react.

This project was built with [Lovable](https://lovable.dev).

**Live app**: https://ivanpalomares-portfolio-ai.lovable.app

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/6d5f44ed-bf5b-4128-8dbd-2f1d98df0a87).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
