# -*- coding: utf-8 -*-
from blocks import h2, p, contact

UPDATED = {"pt":"24 de junho de 2024","en":"June 24, 2024","es":"24 de junio de 2024"}

def _toc(lang):
    T={"pt":["Seus Direitos sob a LGPD","Base Legal para Tratamento","Compartilhamento de Dados","Retenção de Dados","Segurança dos Dados","Encarregado de Dados (DPO)","Contato — Encarregado de Dados"],
       "en":["Your Rights under the LGPD","Legal Basis for Processing","Data Sharing","Data Retention","Data Security","Data Protection Officer (DPO)","Contact — Data Protection Officer"],
       "es":["Sus Derechos bajo la LGPD","Base Legal para el Tratamiento","Compartición de Datos","Retención de Datos","Seguridad de los Datos","Encargado de Datos (DPO)","Contacto — Encargado de Datos"]}
    return [("l%d"%(i+1),x) for i,x in enumerate(T[lang])]

def build_pt():
    b=p("A MyDose está comprometida com a proteção de dados pessoais e em conformidade com a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018).", lead=True)
    b+=h2("Seus Direitos sob a LGPD","l1")
    b+=p("Você tem direito à confirmação da existência de tratamento; acesso aos dados; correção de dados incompletos, inexatos ou desatualizados; anonimização, bloqueio ou eliminação de dados desnecessários; portabilidade dos dados; eliminação dos dados pessoais tratados com consentimento; informação sobre entidades com as quais compartilhamos dados; revogação do consentimento.")
    b+=h2("Base Legal para Tratamento","l2")
    b+=p("Tratamos seus dados pessoais com base no consentimento, execução de contrato, cumprimento de obrigação legal, proteção da vida, exercício regular de direitos em processo judicial, proteção do crédito, legítimo interesse e proteção da saúde.")
    b+=h2("Compartilhamento de Dados","l3")
    b+=p("Compartilhamos dados apenas quando necessário para prestação do serviço, cumprimento de obrigações legais ou com seu consentimento explícito.")
    b+=h2("Retenção de Dados","l4")
    b+=p("Mantemos seus dados pelo tempo necessário para cumprir as finalidades descritas, exceto quando a lei exigir período maior.")
    b+=h2("Segurança dos Dados","l5")
    b+=p("Implementamos medidas técnicas e organizacionais adequadas para proteger seus dados contra acessos não autorizados, destruição, perda, alteração, comunicação ou difusão.")
    b+=h2("Encarregado de Dados (DPO)","l6")
    b+=p("Nosso Encarregado de Proteção de Dados está disponível para esclarecer dúvidas e receber comunicações sobre tratamento de dados pessoais.")
    b+=h2("Contato — Encarregado de Dados","l7")
    b+=p("Para exercer seus direitos ou esclarecer dúvidas sobre proteção de dados:")
    b+=contact([("E-mail",'<a href="mailto:dpo@mydoseapp.com">dpo@mydoseapp.com</a>'),("Telefone","(11) 99999-9999")])
    return b

def build_en():
    b=p("MyDose is committed to protecting personal data and complying with the Brazilian General Data Protection Law (LGPD — Law No. 13.709/2018).", lead=True)
    b+=h2("Your Rights under the LGPD","l1")
    b+=p("You have the right to: confirmation that processing exists; access to your data; correction of incomplete, inaccurate or outdated data; anonymization, blocking or deletion of unnecessary data; data portability; deletion of personal data processed with consent; information about the entities with which we share data; and revocation of consent.")
    b+=h2("Legal Basis for Processing","l2")
    b+=p("We process your personal data based on consent, performance of a contract, compliance with a legal obligation, protection of life, the regular exercise of rights in legal proceedings, credit protection, legitimate interest and protection of health.")
    b+=h2("Data Sharing","l3")
    b+=p("We share data only when necessary to provide the service, to comply with legal obligations, or with your explicit consent.")
    b+=h2("Data Retention","l4")
    b+=p("We keep your data for as long as necessary to fulfill the described purposes, except where the law requires a longer period.")
    b+=h2("Data Security","l5")
    b+=p("We implement appropriate technical and organizational measures to protect your data against unauthorized access, destruction, loss, alteration, communication or dissemination.")
    b+=h2("Data Protection Officer (DPO)","l6")
    b+=p("Our Data Protection Officer is available to answer questions and receive communications about the processing of personal data.")
    b+=h2("Contact — Data Protection Officer","l7")
    b+=p("To exercise your rights or clarify questions about data protection:")
    b+=contact([("E-mail",'<a href="mailto:dpo@mydoseapp.com">dpo@mydoseapp.com</a>'),("Phone","+55 (11) 99999-9999")])
    return b

def build_es():
    b=p("MyDose está comprometida con la protección de datos personales y en cumplimiento de la Ley General de Protección de Datos de Brasil (LGPD — Ley n.º 13.709/2018).", lead=True)
    b+=h2("Sus Derechos bajo la LGPD","l1")
    b+=p("Usted tiene derecho a: la confirmación de la existencia de tratamiento; el acceso a los datos; la corrección de datos incompletos, inexactos o desactualizados; la anonimización, el bloqueo o la eliminación de datos innecesarios; la portabilidad de los datos; la eliminación de los datos personales tratados con consentimiento; información sobre las entidades con las que compartimos datos; y la revocación del consentimiento.")
    b+=h2("Base Legal para el Tratamiento","l2")
    b+=p("Tratamos sus datos personales sobre la base del consentimiento, la ejecución de un contrato, el cumplimiento de una obligación legal, la protección de la vida, el ejercicio regular de derechos en un proceso judicial, la protección del crédito, el interés legítimo y la protección de la salud.")
    b+=h2("Compartición de Datos","l3")
    b+=p("Compartimos datos solo cuando es necesario para la prestación del servicio, el cumplimiento de obligaciones legales o con su consentimiento explícito.")
    b+=h2("Retención de Datos","l4")
    b+=p("Conservamos sus datos por el tiempo necesario para cumplir las finalidades descritas, salvo cuando la ley exija un período mayor.")
    b+=h2("Seguridad de los Datos","l5")
    b+=p("Implementamos medidas técnicas y organizativas adecuadas para proteger sus datos contra accesos no autorizados, destrucción, pérdida, alteración, comunicación o difusión.")
    b+=h2("Encargado de Datos (DPO)","l6")
    b+=p("Nuestro Encargado de Protección de Datos está disponible para aclarar dudas y recibir comunicaciones sobre el tratamiento de datos personales.")
    b+=h2("Contacto — Encargado de Datos","l7")
    b+=p("Para ejercer sus derechos o aclarar dudas sobre protección de datos:")
    b+=contact([("Correo",'<a href="mailto:dpo@mydoseapp.com">dpo@mydoseapp.com</a>'),("Teléfono","+55 (11) 99999-9999")])
    return b

def content(lang):
    b={"pt":build_pt,"en":build_en,"es":build_es}[lang]()
    return UPDATED[lang], b, _toc(lang)
