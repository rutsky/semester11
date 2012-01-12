#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import glob
from textwrap import dedent

articles = [
    ("PavlovS_CraySupercomputers", 
    "Сергей Павлов",
    "Суперкомпьютеры фирмы Cray",
    """Фирма Cray Inc&nbsp;&mdash; &laquo;законодатель мод$raquo; на рынке 
    суперкомпьютеров. Доклад содержит подробное описание архитектуры 
    суперкомпьютеров новейших серий XT6 и XE6. Особое внимание уделено 
    последним изменениям в архитектуре, позволившим вдвое увеличить 
    производительность вычислительных узлов.
    """,
    ),

    ("RutskyV_HowToUse",
    "Владимир Руцкий",
    "Свободный доступ к суперкомпьютерам для решения исследовательских задач",
    """Доклад посвящён обзору доступных для свободного использования 
    высокопроизводительных систем в Российской Федерации. Основная часть 
    доклада посвящена суперкомпьютерному комплексу НИВЦ МГУ: свободно 
    предоставляемые кластером ресурсы, порядок регистрации, архитектура 
    кластера и предоставляемые средства разработки.
    """,
    ),

    ("TsyplyaevA_GPGPU",
    "Александр Цыпляев",
    "General-purpose GPU",
    """General-purpose graphics processing units (GPGPU)&nbsp;&mdash; решение 
    произвольных вычислительных задач с использованием графического процессора.
    В докладе изложена история возникновения этого направления 
    высокопроизводительных вычислений, приведены его основные концепции и 
    техники. Представлены примеры успешного использования графического 
    процессора для решения задач гидроаэродинамики, медицины, 
    томографии и т. д.
    """,
    ),

    ("KononovaA_OpenMP",
    "Анастасия Кононова",
    "Open Multi-Processing",
    """Open Multi-Processing (OpenMP)&nbsp;&mdash; открытый стандарт для 
    распараллеливания C, C++ и Фортран-программ на многопроцессорных 
    системах с общей памятью. В докладе изложена основная модель 
    параллелизма&nbsp;&mdash; модель 
    &laquo;ветвление&ndash;объединение&raquo;&nbsp;&mdash; и перечислены 
    директивы компилятора, библиотечные процедуры и переменные окружения, 
    используемые в OpenMP. Также приведён пример распараллеливания программы 
    средствами OpenMP и сравнение OpenMP с MPI.
    """,
    ),

    ("KononovaA_IBM",
    "Анастасия Кононова",
    "Суперкомпьютеры фирмы IBM",
    """Доклад посвящён архитектуре суперкомпьютеров серии IBM Blue Gene и 
    суперкомпьютера IBM Roadrunner, занявшего первое место в рейтинге 
    Top500 в июне 2009 года. Также представлен список основных достижений 
    компании IBM, среди которых победа шахматного суперкомпьютера IBM Deep Blue 
    над чемпионом мира Гарри Каспаровым в 1997 году.
    """,
    ),

    ("ChukanovV_MapReduce",
    "Вячеслав Чуканов",
    "MapReduce",
    """MapReduce&nbsp;&mdash; программная модель для решения задач обработки 
    больших массивов данных в распределённых системах, представленная в 
    2004 году компанией Google. В докладе приведено подробное описание 
    этой модели и примеры задач, решаемых с её помощью.
    """,
    ),

    ("KirillovaY_MPI",
    "Юлия Кириллова",
    "Message Passing Interface",
    """Message Passing Interface (MPI)&nbsp;&mdash; открытый стандарт написания 
    параллельных программ для систем с распределённой памятью на языках С, С++ 
    и Фортран. В докладе изложена основная модель межпроцессорной 
    коммуникации&nbsp;&mdash; модель передачи сообщений&nbsp;&mdash; и 
    представлено подробное описание библиотечных функций. В заключение приведён 
    пример MPI-программы. 
    """,
    ),

    ("SapozhnikovG_RuSupercomputers",
    "Герман Сапожников",
    "Суперкомпьютеры в России. Российские компании",
    """В докладе приведён анализ российского рынка суперкомпьютеров, 
    перечислены основные проблемы и направления развития отрасли. Подробно 
    освещена деятельность крупнейших российских компаний: Т-платформы, СКИФ, 
    КРОК. 
    """,
    ),

    ("TsyplyaevA_Top500",
    "Александр Цыпляев",
    "Top500",
    """Top500&nbsp;&mdash; это проект по составлению рейтинга и описаний 
    500 самых производительных суперкомпьютеров мира. Доклад посвящён тому, 
    кто и зачем составляет этот рейтинг, как измеряется производительность и 
    какая дополнительная информация включается в описание суперкомпьютеров. 
    Также представлено описание суперкомпьютеров, занявших первые три строки в 
    рейтинге Top500 в июне 2011 года. 
    """,
    ),

    ("FishkovA_Top50CIS",
    "Александр Фишков",
    "Top50 СНГ",
    """Top50&nbsp;&mdash; это проект по составлению рейтинга и описаний 50 
    самых производительных суперкомпьютеров, находящихся на территории СНГ. В 
    докладе объяснено, как измеряется производительность, и приведено 
    подробное описание самого производительного суперкомпьютера 
    СНГ&nbsp;&mdash; &laquo;Ломоносова&raquo;. Также представлена любопытная 
    статистика о производителях процессоров, разработчиках и областях 
    применения суперкомпьютеров из этого рейтинга.
    """,
    ),

    ("LyubomishchenkoN_HPCHPSGI",
    "Николай Любомищенко",
    "Высокопроизводительные системы HP и SGI",
    """Доклад посвящен суперкомпьютерам, разработанным фирмами HP и SGI. 
    Рассматривается архитектура, операционные системы (так называемые 
    кластерные среды), необходимые для работы суперкомпьютеров, а также 
    прикладное ПО, разработанное для работы в кластерной среде. Также 
    приводятся примеры применения данных систем в научных организациях для 
    различных областей науки.
    """,
    ),

    ("LyubomishchenkoN_HPOSSDK",
    "Николай Любомищенко",
    "Высокопроизводительные системы. ОС. Программные средства",
    """Рассмотрены операционные системы, фигурировавшие в списке Top500 в 
    различные годы, составлен их рейтинг. Приведен список распределенных 
    файловых систем. Подробно описано применение такого программного средства, 
    как Hadoop: компоненты для обеспечения работы, процесс установки, фреймворк 
    для распределенного вычисления задач MapReduce.
    """,
    ),

    ("ChukanovV_NetworkCommunications",
    "Вячеслав Чуканов",
    "Сетевая коммуникация в кластерах",
    """В докладе приведены основные принципы передачи данных в компьютерных 
    сетях, и, в частности, внутри кластера. Рассмотрены различные 
    коммуникационные протоколы и типы коммуникаций, такие как Ethernet, 
    Infiniband и т.д., а также сравнение их производительности.
    """,
    ),

    ("TolmachevD_RuConferences",
    "Дмитрий Толмачев",
    "Российские конференции и журналы, посвященные высокопроизводительным вычислениям",
    """В докладе рассказывается о том, какие научные конференции, посвященные 
    высокопроизводительным вычислениям, проводятся в России, в каких городах 
    проводятся эти мероприятия, кто выступает их организатором, какова основная 
    тематика выступлений, и какова цель проведения каждой конференции. Также 
    приведены названия научных журналов, посвященных теме 
    высокопроизводительных вычислений.
    """,
    ),

    ("SidorovskayaA_VoevodinsLecture",
    "Анастасия Сидоровская",
    "Лекция Воеводина В.В. о суперкомпьютерах",
    """В докладе представлен краткий обзор двух лекций, прочитанных профессором 
    МГУ им. Ломоносова Воеводиным В.В. в проекте Academia и посвященных 
    суперкомпьютерам и их месту в современном научном мире. В первой лекции 
    уделяется внимание понятию суперкомпьютер, появление и развитие 
    суперкомпьютеров. Во второй лекции рассказывается о суперкомпьютерных 
    вычислниях, их применении и эффективности.
    """,
    ),

    ("ObraztsovT_DistributedComputations",
    "Тимофей Образцов",
    "Распределенные вычисления",
    """Создание метакомпьютера и распределенные вычисления позволяют 
    использовать колоссальные вычислительные ресурсы компьютерных сетей. 
    Следующий шаг в этом направлении&nbsp;&mdash; облачные вычисления. В 
    докладе рассмотрены принципы организации распределенных и облачных 
    вычислений.
    """,
    ),

    ("FishkovA_DistributedFS",
    "Александр Фишков",
    "Распределенные файловые системы",
    """В докладе приведены такие понятия, как файловый сервис и файловый 
    сервер, а также описаны принцип работы файлового сервера и структура 
    файловой системы. Далее в качестве примера описана Google File System, 
    особенности её работы, архитектура и интерфейс, описание основных 
    компонент.
    """,
    ),

    ("KirillovaY_FlinnTaxonomy",
    "Юлия Кириллова",
    "Таксономия Флинна",
    """Майкл Флинн предложил общую классификацию архитектур ЭВМ по признакам 
    наличия параллелизма в потоках команд и данных. Затем эта классификация 
    была расширена. В докладе описаны основные виды параллелизма программ, 
    их сравнение, а также приведены примеры задач, характерных для того или 
    иного вида. Приведены примеры первых суперкомпьютеров, в архитектуру 
    которых был заложен конкретный вид параллелизма.
    """,
    ),

    ("TolmachevD_CooperativeGames",
    "Дмитрий Толмачев",
    "Разработка и анализ высокопроизводительных алгоритмов решения кооперативных игр",
    """В данном докладе раскрывается тема решения задач из теории игр 
    используя суперкомпьютерные технологии. Для этого приведены основные 
    понятия из теории игр и формальная постановка задачи. Далее приводится 
    алгоритм решения и способы распараллеливания этого алгоритма, а также 
    результаты эффективности распараллеливания.
    """,
    ),
    ]

def article_html(article):
    name, author, title, annotation = article

    num_pages = len(glob.glob("cd/images/presentations/{0}-*.jpg".format(name)))
    images_list = ', '.join(
        ["'images/presentations/{0}-{1}.jpg'".format(name, i) 
            for i in xrange(num_pages)])

    return dedent("""\
      <tr>
        <td>
          <a href="#" onclick="$.prettyPhoto.open([{images_list}], [{titles_list}], [{descriptions_list}]); return false;"><img 
               class="thumb"
               src="images/presentations/thumbs/{name}.jpg" 
                  width="200" height="150" 
                  alt="{title}"></a>
        </td>
        <td>
          <h2><a class="title" href="presentations/{name}.pdf">{title}</a></h2>
          <span class="author">{author}</span>, <a href="presentations/{name}.pdf">PDF</a>
          <div class="annotation">{annotation}</div>
        </td>
      </tr>
    """.format(name=name, title=title, author=author, 
               annotation=annotation, images_list=images_list,
               titles_list=', '.join(["''"] * num_pages), 
               descriptions_list=', '.join(["''"] * num_pages)))

def main():
    sorted_articles = sorted(articles, key=lambda x: x[2])

    articles_html = ''.join(map(article_html, sorted_articles))

    with open('index_template.html', 'rt') as f:
        html = f.read()

    html = html.replace("<!-- ARTICLES HTML -->\n", articles_html)

    with open('cd/index.html', 'wt') as f:
        f.write(html)

if __name__ == "__main__":
    main()
