# -*- coding: utf-8 -*-
from blocks import h2, h3, p, ul, callout, contact

UPDATED = {"pt":"05 de janeiro de 2026","en":"January 5, 2026","es":"5 de enero de 2026"}

def _toc(lang):
    T={
     "pt":["Aceitação dos Termos","Definições","O que é o MyDose","Código de Adesão","Serviços Prestados","Planos e Cancelamento","Obrigações e Responsabilidades","Limitação de Responsabilidade","MyDose Inteligência Artificial","Marketing Digital","Consentimento","Propriedade Intelectual","Suporte e Contato","Conteúdo da Comunidade"],
     "en":["Acceptance of Terms","Definitions","What MyDose Is","Membership Code","Services Provided","Plans and Cancellation","Obligations and Responsibilities","Limitation of Liability","MyDose Artificial Intelligence","Digital Marketing","Consent","Intellectual Property","Support and Contact","Community Content"],
     "es":["Aceptación de los Términos","Definiciones","Qué es MyDose","Código de Adhesión","Servicios Prestados","Planes y Cancelación","Obligaciones y Responsabilidades","Limitación de Responsabilidad","MyDose Inteligencia Artificial","Marketing Digital","Consentimiento","Propiedad Intelectual","Soporte y Contacto","Contenido de la Comunidad"],
    }
    return [("s%d"%(i+1),lbl) for i,lbl in enumerate(T[lang])]

SEC={"pt":"Seção","en":"Section","es":"Sección"}

def build_pt():
    S=SEC["pt"]; b=""
    b+=p("Estes Termos e Condições se aplicam ao app MyDose e à plataforma web MyDose, solução oferecida pela My Dose LLC, empresa constituída em Delaware — Estados Unidos. Ao utilizar a plataforma, você concorda tácita e inteiramente com as disposições aqui contidas. Se não estiver confortável em aceitar estes T&C, não poderá usar a plataforma e os serviços do MyDose.", lead=True)
    b+=h2("Aceitação dos Termos e Condições","s1",cap=S+" 1")
    b+=p("1.1. Estes T&C contêm informações importantes e o usuário deve lê-los antes de solicitar a ativação de sua adesão ao aplicativo.")
    b+=p('1.2. A versão atualizada está disponível em nossos portais ou pelo e-mail <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.')
    b+=p("1.3. Quando você marca 'Li e estou de acordo', está dizendo que leu, entendeu e concorda em seguir as regras.")
    b+=p("1.4. O MyDose pode modificar estes T&C a qualquer momento. Sempre que houver atualização significativa, informaremos via e-mail ou notificações na plataforma.")
    b+=p("1.5. Requisitos para cadastro: fornecer e-mail válido, número de identificação, e declarar estar em condições físicas e mentais para participar das Comunidades.")
    b+=p("1.6. Menores de 18 anos ('Usuários Menores') precisam do consentimento expresso do responsável legal através de 'Conta Vinculada'.")
    b+=h2("Definições","s2",cap=S+" 2")
    b+=ul(["<strong>Conteúdo:</strong> tudo que os usuários compartilham (textos, fotos, vídeos, áudios, e-books)","<strong>Comunidade:</strong> espaço virtual para compartilhar hábitos saudáveis","<strong>Comunidade Privada:</strong> criada por Líderes para impulsionar seus negócios","<strong>Comunidade Pública:</strong> aberta ao público","<strong>Plataforma MyDose:</strong> aplicações para jornadas de bem-estar físico, nutricional e mental","<strong>Usuário:</strong> pessoa física com perfil na plataforma","<strong>Usuário Líder:</strong> pessoa que contrata plano de assinatura para criar Comunidades","<strong>Usuário Gestor:</strong> pessoa que auxilia o Líder na gestão da Comunidade"])
    b+=h2("O que é o MyDose","s3",cap=S+" 3")
    b+=p("3.1. A Plataforma MyDose oferece jornadas de bem-estar físico, nutricional e mental, bem como orientações de saúde.")
    b+=p("3.2. O usuário pode compartilhar sua jornada e evolução com outros usuários, gerando engajamento e potencializando práticas saudáveis.")
    b+=p("3.3. O MyDose acredita na força da Comunidade e no poder de colaboração para criar e manter hábitos saudáveis.")
    b+=p("3.4. O MyDose é uma plataforma digital focada no gerenciamento eficiente de Comunidades online, fornecendo ferramentas para criação, personalização e administração.")
    b+=h2("Código de Adesão","s4",cap=S+" 4")
    b+=p("4.1. O código de adesão é o e-mail do Usuário.")
    b+=p("4.2. A adesão é pessoal e intransferível. O Usuário é responsável pela guarda do código, sendo vedada divulgação a terceiros.")
    b+=p("4.3. O Usuário deve comunicar imediatamente o MyDose sobre uso não autorizado.")
    b+=p("4.4. O Usuário concorda em:")
    b+=ul(["Não usar a plataforma para fins fraudulentos ou ilegais","Notificar sobre uso não autorizado","Solicitar nova senha se suspeitar comprometimento","Usar a plataforma de boa-fé"])
    b+=h2("Serviços Prestados","s5",cap=S+" 5")
    b+=p("5.1. O MyDose concede licença pessoal, não exclusiva e intransferível para usar os Serviços.")
    b+=p("5.2. A plataforma permite:")
    b+=ul(["Criação e gestão de Comunidades gamificadas","Ferramentas para mudanças comportamentais","Sistema de recompensas e reconhecimento","Analytics e relatórios de progresso","Integração com ferramentas de terceiros","Interações com inteligência artificial","Recursos de comunicação e engajamento"])
    b+=p("5.3. Novas funcionalidades podem ser adicionadas e existentes modificadas a qualquer momento.")
    b+=h2("Planos e Cancelamento","s6",cap=S+" 6")
    b+=p("6.1. Usuários podem participar gratuitamente de Comunidades Públicas e Privadas.")
    b+=p("6.2. Usuários Líderes contratam planos de assinatura (mensal, trimestral, semestral ou anual).")
    b+=p("6.3. Todos os planos RENOVAM-SE AUTOMATICAMENTE até pedido de cancelamento.")
    b+=p("7.1. Usuários Líderes podem cancelar a qualquer momento, com efeitos até a próxima recorrência.")
    b+=p("7.2. Reembolso disponível em até 7 dias do pagamento. Após este prazo, não há reembolso.")
    b+=p('7.5. PEDIDOS DE CANCELAMENTO devem ser enviados por e-mail para <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a> com 20 dias de antecedência da renovação.')
    b+=h2("Obrigações e Responsabilidades","s7",cap=S+" 7")
    b+=p("8.1. O usuário é responsável por todas as manifestações, conteúdos inseridos e interações realizadas.")
    b+=p("8.2. Condutas vedadas incluem:")
    b+=ul(["Publicar informações incorretas ou criar identidade falsa","Usar conta de outra pessoa","Realizar engenharia reversa do aplicativo","Interferir no funcionamento ou segurança","Acessar áreas não autorizadas","Usar bots, scripts ou raspagem de dados","Assediar ou prejudicar outros usuários","Violar direitos de propriedade intelectual"])
    b+=p("8.3. Conteúdos proibidos: dados de terceiros sem autorização, conteúdo ilegal, discriminatório, vírus ou malwares.")
    b+=h2("Limitação de Responsabilidade","s8",cap=S+" 8")
    b+=p("9.1. O MyDose não é responsável por dados incorretos ou incompletos fornecidos.")
    b+=p("9.2. O aplicativo NÃO substitui atendimento médico, nutricionista ou profissional de saúde. O Usuário é responsável pela própria saúde.")
    b+=p("9.3. O MyDose se isenta de responsabilidade por atos de Usuários Líderes e Usuários que causem danos.")
    b+=p("9.4. O MyDose não é responsável por conteúdos postados nas Comunidades.")
    b+=p("9.5. Contratos entre Usuários Líderes e Usuários não vinculam o MyDose.")
    b+=p("9.10. Usuários Líderes são responsáveis por administrar suas comunidades de forma ética e por todo relacionamento com seus Usuários.")
    b+=h2("MyDose Inteligência Artificial","s9",cap=S+" 9")
    b+=p("10.1. Partes dos serviços podem incluir tecnologias de inteligência artificial ou aprendizado de máquina.")
    b+=p("10.2. O MyDose trabalha para tornar os serviços mais precisos e confiáveis. No entanto, resultados podem não refletir com precisão pessoas, locais ou fatos reais.")
    b+=p("10.3. Os usuários entendem que:")
    b+=ul(["Resultados podem conter erros ou informações incorretas","Não devem confiar nos resultados como fonte única de informações","Devem avaliar a precisão antes de utilizar ou compartilhar","Resultados podem ser incompletos, incorretos ou ofensivos"])
    b+=h2("Marketing Digital","s10",cap=S+" 10")
    b+=p("11.1. Ao se registrar, o Usuário reconhece que pode receber materiais promocionais de marketing dos nossos parceiros estratégicos.")
    b+=p('11.2. O Usuário pode optar por não receber comunicações enviando solicitação para <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.')
    b+=p("11.3. O MyDose poderá enviar comunicações via redes sociais (Facebook, Instagram, Google, LinkedIn) e WhatsApp.")
    b+=h2("Consentimento","s11",cap=S+" 11")
    b+=p("12.1. O Usuário consente em receber documentos e informações por comunicação eletrônica.")
    b+=p("12.2. O MyDose pode contatar via e-mail, SMS, notificações push, WhatsApp e telefone.")
    b+=p("12.2.1. O Usuário consente que o MyDose e os Usuários Líderes possam usar e compartilhar suas informações pessoais para exames e estudos de saúde.")
    b+=p("12.2.3. O MyDose pode compartilhar dados anonimizados com parceiros para análises de perfil, estudos analíticos e campanhas de marketing.")
    b+=h2("Propriedade Intelectual","s12",cap=S+" 12")
    b+=p("12.1. O MyDose pode usar a marca do Usuário Líder em seu portfólio para divulgação.")
    b+=p("12.2. O MyDose e usuários se comprometem a não prejudicar os direitos de propriedade intelectual.")
    b+=p("12.3. Todos os direitos de Propriedade Intelectual do aplicativo são do MyDose ou licenciados a ele.")
    b+=p("12.4. Nenhuma disposição transfere direitos de patente, segredo de negócio, código-fonte, designs, sistemas tecnológicos ou inteligência artificial do MyDose aos usuários.")
    b+=h2("Suporte e Contato","s13",cap=S+" 13")
    b+=p("O MyDose oferece suporte aos Usuários Líderes para questões técnicas e orientações. Usuários devem procurar suporte diretamente com os Usuários Líderes de suas Comunidades.")
    b+=contact([("E-mail",'<a href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>'),("Horário","9h às 17h, seg. a sex."),("Empresa","My Dose LLC — Delaware, EUA")])
    b+=h2("Conteúdo da Comunidade","s14",cap=S+" 14")
    b+=p("Ao utilizar as funcionalidades de comunidade e compartilhamento do MyDose, o usuário concorda em não publicar conteúdo ofensivo, odioso, sexualmente explícito ou violento. Reservamo-nos o direito de remover qualquer conteúdo denunciado em até 24 horas e banir usuários que violem estas regras, mantendo uma política de tolerância zero para abusos.")
    return b

def content(lang):
    if lang=="pt":
        return UPDATED["pt"], build_pt(), _toc("pt")
    from content_termos_tr import build as build_tr
    return UPDATED[lang], build_tr(lang), _toc(lang)
