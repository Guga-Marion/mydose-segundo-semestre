# -*- coding: utf-8 -*-
"""Página de Contato — captação de leads, dúvidas e currículos. 3 línguas (PT oficial)."""
from blocks import p, raw

T = {
 "pt":{"lead":"Fale com a MyDose. Quer criar sua comunidade, tirar uma dúvida, falar com o suporte, trabalhar com a gente ou falar com a imprensa? É por aqui.",
       "email_k":"E-mail","phone_k":"Telefone","wa_k":"WhatsApp","wa_v":"Falar no WhatsApp",
       "f_name":"Nome","f_email":"E-mail","f_phone":"Telefone / WhatsApp","f_subject":"Assunto","f_msg":"Mensagem",
       "opts":["Quero criar minha comunidade","Dúvida ou suporte","Trabalhe conosco (currículo)","Imprensa","Outro"],
       "send":"Enviar mensagem","ph_msg":"Conte pra gente como podemos ajudar…",
       "ok":"Abrimos seu app de e-mail com a mensagem pronta. É só enviar! Se preferir, escreva direto para contact@mydoseapp.com.",
       "priv":"🔒 Seus dados são usados só para responder seu contato. Para vagas, anexe seu currículo ao e-mail."},
 "en":{"lead":"Get in touch with MyDose. Want to create your community, ask a question, reach support, work with us or talk to the press? Right here.",
       "email_k":"E-mail","phone_k":"Phone","wa_k":"WhatsApp","wa_v":"Chat on WhatsApp",
       "f_name":"Name","f_email":"E-mail","f_phone":"Phone / WhatsApp","f_subject":"Subject","f_msg":"Message",
       "opts":["I want to create my community","Question or support","Work with us (résumé)","Press","Other"],
       "send":"Send message","ph_msg":"Tell us how we can help…",
       "ok":"We opened your e-mail app with the message ready. Just hit send! You can also write directly to contact@mydoseapp.com.",
       "priv":"🔒 Your data is used only to reply to your message. For job openings, attach your résumé to the e-mail."},
 "es":{"lead":"Ponte en contacto con MyDose. ¿Querés crear tu comunidad, hacer una consulta, hablar con soporte, trabajar con nosotros o con la prensa? Es por acá.",
       "email_k":"Correo","phone_k":"Teléfono","wa_k":"WhatsApp","wa_v":"Escribir por WhatsApp",
       "f_name":"Nombre","f_email":"Correo","f_phone":"Teléfono / WhatsApp","f_subject":"Asunto","f_msg":"Mensaje",
       "opts":["Quiero crear mi comunidad","Consulta o soporte","Trabajá con nosotros (CV)","Prensa","Otro"],
       "send":"Enviar mensaje","ph_msg":"Contanos cómo podemos ayudar…",
       "ok":"Abrimos tu app de correo con el mensaje listo. ¡Solo enviálo! También podés escribir directo a contact@mydoseapp.com.",
       "priv":"🔒 Tus datos se usan solo para responder tu contacto. Para vacantes, adjuntá tu CV al correo."},
}

def content(lang):
    t=T[lang]
    b=p(t["lead"], lead=True)
    # canais diretos
    alt=('<div class="contact-alt">'
      '<a href="mailto:contact@mydoseapp.com"><span class="ic">✉️</span><span><span class="k">%s</span><div class="v">contact@mydoseapp.com</div></span></a>'
      '<a href="tel:+14245372605"><span class="ic">📞</span><span><span class="k">%s</span><div class="v">+1 424-537-2605</div></span></a>'
      '<a href="https://wa.me/14245372605" target="_blank" rel="noopener"><span class="ic">💬</span><span><span class="k">%s</span><div class="v">%s</div></span></a>'
      '</div>') % (t["email_k"], t["phone_k"], t["wa_k"], t["wa_v"])
    b+=raw(alt)
    opts="".join('<option>%s</option>'%o for o in t["opts"])
    form=('<form class="cform" data-to="contact@mydoseapp.com">'
      '<div class="row two">'
      '<label>%s<input name="nome" required></label>'
      '<label>%s<input type="email" name="email" required></label></div>'
      '<div class="row two">'
      '<label>%s<input name="telefone"></label>'
      '<label>%s<select name="assunto">%s</select></label></div>'
      '<label>%s<textarea name="mensagem" placeholder="%s" required></textarea></label>'
      '<button class="btn-submit" type="submit">%s</button>'
      '<p class="ok">%s</p>'
      '<p class="m-priv">%s</p>'
      '</form>') % (t["f_name"],t["f_email"],t["f_phone"],t["f_subject"],opts,
                    t["f_msg"],t["ph_msg"],t["send"],t["ok"],t["priv"])
    b+=raw(form)
    return None, b, None  # sem "atualização", sem TOC

def build(lang):
    return content(lang)[1]
