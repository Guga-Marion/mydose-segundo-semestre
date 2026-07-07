# -*- coding: utf-8 -*-
"""Central de Ajuda — FAQ do site v3 (conteúdo real MyDose), nas 3 línguas."""
from blocks import p, raw, faq, contact

LEAD={"pt":"Encontre respostas para as principais dúvidas sobre o MyDose. Não achou o que procurava? Fale com a gente.",
      "en":"Find answers to the main questions about MyDose. Didn't find what you were looking for? Talk to us.",
      "es":"Encontrá respuestas a las principales dudas sobre MyDose. ¿No encontraste lo que buscabas? Hablá con nosotros."}
SEARCH_PH={"pt":"Buscar na Central de Ajuda…","en":"Search the Help Center…","es":"Buscar en el Centro de Ayuda…"}
EMPTY={"pt":"Nenhum resultado. Tente outro termo ou fale com o suporte.","en":"No results. Try another term or contact support.","es":"Sin resultados. Probá otro término o contactá al soporte."}
STILL={"pt":"Ainda com dúvidas?","en":"Still have questions?","es":"¿Todavía con dudas?"}
STILL_TXT={"pt":'Fale com o nosso time pela <a class="inl" href="%s">página de contato</a> ou pelo e-mail <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.',
           "en":'Talk to our team via the <a class="inl" href="%s">contact page</a> or by e-mail at <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.',
           "es":'Hablá con nuestro equipo en la <a class="inl" href="%s">página de contacto</a> o por correo a <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.'}
CONTATO={"pt":"contato.html","en":"contato-en.html","es":"contato-es.html"}

FAQS={
"pt":[
 ("Preciso entender de tecnologia ou marketing?","Não. No <b>Software</b> você tem tudo pronto e simples; nos planos com serviço (Co-pilot, Autopilot, Partner), a gente cuida do conteúdo, do tráfego e da estratégia por você. <b>Você só cuida das pessoas.</b>"),
 ("Tenho poucos pacientes hoje. Ainda vale?","Sim — é exatamente quando mais compensa. A comunidade aumenta a adesão e a recompra dos que você já tem, e a esteira de produtos cria receita <b>sem você precisar de mais horários</b>."),
 ("E a ética e o sigilo, principalmente na saúde mental?","A IA é treinada nos seus limites, com <b>ética e sigilo</b>. Ela mantém o vínculo entre as sessões sem substituir o seu trabalho clínico — você define o tom e as regras."),
 ("Tem fidelidade ou multa?","<b>Sem fidelidade-armadilha.</b> E você tem 30 dias de garantia: se não curtir, devolvemos 100% do investimento, sem perguntas."),
 ("Em quanto tempo vejo resultado?","Nossa promessa: em <b>30 dias</b> você faz a sua 1ª venda dentro do MyDose e tem pacientes usando os seus protocolos — <b>ou a gente trabalha de graça até acontecer</b>."),
 ("A verba de mídia está inclusa no preço?","Não, e isso é de propósito: a mídia fica <b>transparente e sob seu controle</b>, fora da mensalidade. Você sempre sabe quanto vai pra anúncio."),
],
"en":[
 ("Do I need to understand tech or marketing?","No. With <b>Software</b> everything is ready and simple; on service plans (Co-pilot, Autopilot, Partner) we handle content, ads and strategy for you. <b>You just care for people.</b>"),
 ("I have few patients today. Is it still worth it?","Yes — that's exactly when it pays off most. The community boosts adherence and repeat sales from patients you already have, and the product ladder creates revenue <b>without needing more slots</b>."),
 ("What about ethics and confidentiality, especially in mental health?","The AI is trained within your limits, with <b>ethics and confidentiality</b>. It keeps the bond between sessions without replacing your clinical work — you set the tone and the rules."),
 ("Any lock-in or cancellation fee?","<b>No lock-in traps.</b> And you get a 30-day guarantee: if you don't love it, we refund 100%, no questions asked."),
 ("How soon do I see results?","Our promise: within <b>30 days</b> you make your first sale inside MyDose and have patients using your protocols — <b>or we work for free until it happens</b>."),
 ("Is the ad budget included in the price?","No — on purpose: ad spend stays <b>transparent and under your control</b>, outside the subscription. You always know how much goes to ads."),
],
"es":[
 ("¿Necesito saber de tecnología o marketing?","No. En <b>Software</b> tenés todo listo y simple; en los planes con servicio (Co-pilot, Autopilot, Partner) nos encargamos del contenido, del tráfico y de la estrategia por vos. <b>Vos solo cuidás a las personas.</b>"),
 ("Tengo pocos pacientes hoy. ¿Igual sirve?","Sí — es justo cuando más conviene. La comunidad sube la adherencia y la recompra de los que ya tenés, y la línea de productos crea ingresos <b>sin que necesites más turnos</b>."),
 ("¿Y la ética y la confidencialidad, sobre todo en salud mental?","La IA se entrena en tus límites, con <b>ética y confidencialidad</b>. Mantiene el vínculo entre sesiones sin reemplazar tu trabajo clínico — vos definís el tono y las reglas."),
 ("¿Hay permanencia o multa?","<b>Sin cláusulas trampa.</b> Y tenés 30 días de garantía: si no te gusta, te devolvemos el 100%, sin preguntas."),
 ("¿En cuánto tiempo veo resultados?","Nuestra promesa: en <b>30 días</b> hacés tu primera venta dentro de MyDose y tenés pacientes usando tus protocolos — <b>o trabajamos gratis hasta que pase</b>."),
 ("¿La pauta está incluida en el precio?","No, y es a propósito: la pauta queda <b>transparente y bajo tu control</b>, fuera de la mensualidad. Siempre sabés cuánto va a anuncios."),
],
}

def content(lang):
    b=p(LEAD[lang], lead=True)
    b+=raw('<div class="help-search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg><input type="search" placeholder="%s" aria-label="%s"></div>' % (SEARCH_PH[lang], SEARCH_PH[lang]))
    b+=faq(FAQS[lang], empty_msg=EMPTY[lang])
    from blocks import h2
    b+=h2(STILL[lang],"ajuda-contato")
    b+=p(STILL_TXT[lang] % CONTATO[lang])
    return None, b, None  # sem "atualização", sem TOC
