import { useState } from "react";
import i18n from '../i18n';
import { useTranslation, I18nextProvider } from 'react-i18next';
import { createFileRoute } from "@tanstack/react-router";
import {
  GraduationCap,
  PenLine,
  Brain,
  Mail,
  Linkedin,
  Github,
  ArrowRight,
  BookOpen,
  Users,
  Building2,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { Reveal } from "@/components/Reveal";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Iván Palomares — Formación e IA para empresas" },
      {
        name: "description",
        content:
          "PhD en IA. Formación corporativa en Machine Learning y IA Generativa, tech writing especializado y consultoría en datos e IA.",
      },
      { property: "og:title", content: "Iván Palomares — Formación e IA para empresas" },
      {
        property: "og:description",
        content:
          "PhD en IA. Formación corporativa en Machine Learning y IA Generativa, tech writing especializado y consultoría en datos e IA.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Index,
});

const services = [
  {
    icon: GraduationCap,
    title: "Formación Corporativa Global",
    text: "Diseño e imparto programas a medida sobre Python, Machine Learning, LLMs y automatización (n8n) para capacitar a equipos técnicos y de negocio, presencial u online.",
  },
  {
    icon: PenLine,
    title: "Tech Writing y Divulgación",
    text: "Redacción experta de artículos y documentación técnica sobre IA. Autor en plataformas de referencia mundial como Machine Learning Mastery y KDnuggets.",
  },
  {
    icon: Brain,
    title: "Consultoría en IA y Datos",
    text: "Asesoramiento estratégico para integrar soluciones basadas en IA y automatización de flujos que resuelvan problemas reales de negocio.",
  },
];

const milestones = [
  {
    icon: BookOpen,
    title: "Lead Tech Writer",
    text: "Autor principal de contenidos avanzados (NLP, LLMs) para audiencias globales en Machine Learning Mastery, KDnuggets y DataCamp.",
  },
  {
    icon: Users,
    title: "Instructor y Profesor Internacional",
    text: "Diseño e impartición de formaciones B2B para ejecutivos y equipos técnicos en instituciones como EU Business School, EAE y empresas multinacionales.",
  },
  {
    icon: Building2,
    title: "Liderazgo Corporativo en IA",
    text: "Experiencia dirigiendo estrategias de IA Generativa y MLOps como Ex-Head of AI en Loyal Guru y Senior Manager en Capgemini.",
  },
];

const navLinks = [
  { href: "#servicios", label: "nav_servicios" },
  { href: "#experiencia", label: "nav_experiencia" },
  { href: "#sobre-mi", label: "nav_sobre_mi" },
  { href: "#contacto", label: "nav_contacto" },
];

function PageContent() {
  const { t, i18n: i18nInstance } = useTranslation();

  const toggleLanguage = () => {
    const newLang = i18nInstance.language === 'es' ? 'en' : 'es';
    i18nInstance.changeLanguage(newLang);
  };
  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="fixed inset-x-0 top-0 z-50 border-b border-border/60 bg-background/80 backdrop-blur-md">
        <nav className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6">
          <a href="#inicio" className="text-sm font-semibold tracking-tight">
            Iván Palomares<span className="text-primary">, PhD</span>
          </a>
          <div className="hidden items-center gap-8 md:flex">
            {navLinks.map((l) => (
              <a
                key={l.href}
                href={l.href}
                className="text-sm text-muted-foreground transition-colors hover:text-primary"
              >
                {l.label}
              </a>
            ))}
          </div>
          
          {/* Contenedor nuevo para agrupar idioma y botón de contacto */}
          <div className="flex items-center gap-4">
            <button 
              onClick={toggleLanguage} 
              type="button"
              className="flex cursor-pointer items-center gap-2 rounded-full border border-border bg-card px-3 py-1.5 text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
            >
              🌐 {i18nInstance.language === 'es' ? 'EN' : 'ES'}
            </button>
            <Button asChild variant="hero" size="sm">
              <a href="#contacto">Contactar</a>
            </Button>
          </div>
        </nav>
      </header>

      <main>
        {/* HERO */}
        <section id="inicio" className="hero-glow relative overflow-hidden pt-40 pb-28">
          <div className="mx-auto max-w-4xl px-6 text-center">
            <p className="animate-fade-up mb-6 inline-flex items-center gap-2 rounded-full border border-border bg-card px-4 py-1.5 text-xs font-medium tracking-wide text-muted-foreground uppercase">
              PhD. Formador y Divulgador Tech
            </p>
            <h1 className="animate-fade-up text-4xl leading-[1.1] font-semibold tracking-tight text-balance sm:text-5xl md:text-6xl">
              Estrategia, Formación y Divulgación en IA y Datos:{" "}
              <span className="text-primary">Rigor Técnico, Adopción, e Impacto de Negocio.</span>
            </h1>
            <p className="animate-fade-up mx-auto mt-8 max-w-2xl text-base leading-relaxed text-muted-foreground sm:text-lg">
              Soy Iván Palomares, PhD en IA. Ayudo a empresas, profesionales, y organizaciones a dominar el Machine Learning, la IA,
              y los Datos, mediante formación corporativa de alto impacto, la divulgación y creación de contenido
              técnico especializado (Tech Writing).
            </p>
            <div className="animate-fade-up mt-10 flex justify-center">
              <Button asChild variant="hero" size="xl">
                <a href="#contacto">
                  Hablemos de tu proyecto <ArrowRight />
                </a>
              </Button>
            </div>
          </div>
        </section>

        {/* SERVICIOS */}
        <section id="servicios" className="border-t border-border/60 py-24">
          <div className="mx-auto max-w-6xl px-6">
            <Reveal>
              <h2 className="text-3xl font-semibold tracking-tight sm:text-4xl">
                Soluciones que ofrezco
              </h2>
              <p className="mt-5 max-w-3xl text-muted-foreground">
                Con más de 15 años de experiencia tecnológica, trabajo en la intersección entre la
                tecnología profunda y el valor empresarial. Estas son mis áreas de especialidad:
              </p>
            </Reveal>

            <div className="mt-14 grid gap-6 md:grid-cols-3">
              {services.map((s, i) => (
                <Reveal key={s.title} delay={i * 120}>
                  <article className="group h-full rounded-2xl border border-border bg-card p-8 transition-all duration-300 hover:-translate-y-1 hover:border-primary/60 hover:shadow-[var(--shadow-glow)]">
                    <div className="mb-6 inline-flex size-12 items-center justify-center rounded-xl bg-secondary text-primary transition-colors group-hover:bg-primary group-hover:text-primary-foreground">
                      <s.icon className="size-6" />
                    </div>
                    <h3 className="text-lg font-semibold">{s.title}</h3>
                    <p className="mt-3 text-sm leading-relaxed text-muted-foreground">{s.text}</p>
                  </article>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        {/* EXPERIENCIA */}
        <section id="experiencia" className="border-t border-border/60 py-24">
          <div className="mx-auto max-w-4xl px-6">
            <Reveal>
              <h2 className="text-3xl font-semibold tracking-tight sm:text-4xl">
                Experiencia destacada
              </h2>
            </Reveal>
            <ol className="mt-14 space-y-10 border-l border-border pl-8">
              {milestones.map((m, i) => (
                <Reveal key={m.title} delay={i * 120}>
                  <li className="relative">
                    <span className="absolute top-1 -left-[3.05rem] inline-flex size-9 items-center justify-center rounded-full border border-primary/50 bg-background text-primary">
                      <m.icon className="size-4" />
                    </span>
                    <h3 className="text-lg font-semibold">{m.title}</h3>
                    <p className="mt-2 leading-relaxed text-muted-foreground">{m.text}</p>
                  </li>
                </Reveal>
              ))}
            </ol>
          </div>
        </section>

        {/* SOBRE MÍ */}
        <section id="sobre-mi" className="border-t border-border/60 py-24">
          <div className="mx-auto max-w-4xl px-6">
            <Reveal>
              <div className="rounded-3xl border border-border bg-card p-10 sm:p-14">
                <h2 className="text-3xl font-semibold tracking-tight text-balance sm:text-4xl">
                  La IA no es magia, es <span className="text-primary">ingeniería</span>.
                </h2>
                <p className="mt-6 leading-relaxed text-muted-foreground">
                  Soy Doctor (PhD) en Inteligencia Artificial. Durante la actual euforia generativa,
                  aporto el rigor de mi perfil académico (ex-profesor universitario e investigador
                  internacional) combinado con mi experiencia en consultoría corporativa. Trabajo
                  con fluidez en español e inglés, convencido de que el éxito de cualquier modelo
                  predictivo o sistema generativo reside en una base absoluta: la calidad de los
                  datos.
                </p>
              </div>
            </Reveal>
          </div>
        </section>

        {/* CONTACTO */}
        <section id="contacto" className="border-t border-border/60 py-24">
          <div className="mx-auto max-w-2xl px-6">
            <Reveal>
              <h2 className="text-center text-3xl font-semibold tracking-tight sm:text-4xl">
                Hablemos
              </h2>
              <p className="mx-auto mt-5 max-w-xl text-center text-muted-foreground">
                ¿Necesitas una voz experta para tus publicaciones técnicas o un formador que
                capacite a tu equipo? Hablemos.
              </p>
            </Reveal>

            <Reveal delay={120}>
              <form
                action="https://formsubmit.co/gakudo.learn@gmail.com"
                method="POST"
                className="mt-12 space-y-6 rounded-2xl border border-border bg-card p-8"
              >
                <input
                  type="hidden"
                  name="_subject"
                  value="Nuevo contacto desde la web freelance"
                />
                <input type="hidden" name="_captcha" value="false" />

                <div className="space-y-2">
                  <Label htmlFor="name">Nombre completo</Label>
                  <Input id="name" name="name" type="text" required placeholder="Tu nombre" />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="email">Email</Label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    required
                    placeholder="tu@empresa.com"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="message">Tu consulta</Label>
                  <Textarea
                    id="message"
                    name="message"
                    required
                    rows={5}
                    placeholder="Cuéntame brevemente tu proyecto o necesidad de formación."
                  />
                </div>
                <Button type="submit" variant="hero" size="xl" className="w-full">
                  <Mail /> Enviar mensaje
                </Button>
              </form>
            </Reveal>
          </div>
        </section>
      </main>

      <footer className="border-t border-border/60 py-10">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-6 px-6 sm:flex-row">
          <p className="text-sm text-muted-foreground">
            © {new Date().getFullYear()} Iván Palomares. Todos los derechos reservados.
          </p>
          <div className="flex items-center gap-3">
            <a
              href="https://www.linkedin.com/in/ivanpc"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="LinkedIn"
              className="inline-flex size-10 items-center justify-center rounded-lg border border-border text-muted-foreground transition-colors hover:border-primary hover:text-primary"
            >
              <Linkedin className="size-5" />
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default function Index() {
  return (
    <I18nextProvider i18n={i18n}>
      <PageContent />
    </I18nextProvider>
  );
}
