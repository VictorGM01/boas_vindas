import webbrowser as wb
import PySimpleGUI as sg


class BoasVindas:

    def __init__(self):
        janela1 = self.chama_janela_inicial()
        self.janela1 = janela1
        self.chama_as_janelas_correspondentes()

    @staticmethod
    def chama_janela_inicial():
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Seja bem-vindo ao meu perfil',
                     font=('Times New Roman', 25), justification='c')],
            [sg.Text('Detalhar Repositórios', size=(25, 1),
                     font=('Times New Roman', 12)),
             sg.Checkbox('', default=False, key='repositorios')],
            [sg.Text('Sobre mim - Perfil', size=(25, 1),
                     font=('Times New Roman', 12)),
             sg.Checkbox('', default=False, key='perfil')],
            [sg.Text('Linguagens mais usadas', size=(25, 1),
                     font=('Times New Roman', 12)),
             sg.Checkbox('', default=False, key='linguagens')],
            [sg.Text('Assuntos', size=(25, 1), font=('Times New Roman', 12)),
             sg.Checkbox('', default=False, key='assuntos')],
            [sg.Text('')],
            [sg.Button('', image_filename=r'icons\btn_ok.png', key='ok'),
             sg.Button('', image_filename='icons\clear.png', key='x'),
             sg.Button('', image_filename='icons\icon_help.png', key='ajuda')]
        ]

        return sg.Window('Home', layout,
                         element_justification='c', finalize=True)

    def chama_as_janelas_correspondentes(self):
        while True:
            janela, evento, valores = sg.read_all_windows()

            if evento == sg.WINDOW_CLOSED or evento == 'x':
                break

            if evento == 'ok':
                if valores['repositorios']:
                    self.janela1.close()
                    return Repositorios()

class Repositorios:
    def __init__(self):
        # chama janelas
        janela_cybersecurity = self.janela_repositorio_cybersecurity()
        self.janela_cybersecurity = janela_cybersecurity
        self.chama_janelas()
        janela_interfaces_graficas = None
        janela_dicionario_html = None
        janela_mais_repositorios = None

        # referencia janelas
        self.janela_interfaces_graficas = janela_interfaces_graficas
        self.janela_dicionario_html = janela_dicionario_html
        self.janela_mais_repositorios = janela_mais_repositorios

    @staticmethod
    def janela_repositorio_cybersecurity():
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Cybersecurity', font=('Times New Roman', 20)),
             sg.Image(filename='icons\icon_cybersecurity.png')],
            [sg.Text('Este repositório tem como objetivo relacionar a ' +
                     'linguagem de programação Python com a ' +
                     'Segurança Cibernética')],
            [sg.Text('Contém scripts em Python que visam aplicar os conceitos'
                     + ' de cibersegurança por meio da programação')],
            [sg.Text('')],
            [sg.Text('Conteúdo:')],
            [sg.Image(filename='icons\icon_p_blue.png'),
             sg.Listbox(['Keylogger', 'Gerador de senha', 'Gerador de Hash',
                         'Comparador de Hashes', 'Criptografador de arquivos',
                         'Descriptografador de arquivos',
                         'Criptografador da Cifra de César',
                         'Descriptografador da Cifra de César'], size=(35, 1),
                        font=('Times New Roman', 12)),
             sg.Image(filename='icons\icon_p_blue.png')],
            [sg.Text('')],
            [sg.Button('', image_filename=r'icons\btn_icon_home.png',
                       key='home'),
             sg.Button('', image_filename=r'icons\btn_github.png', key='git'),
             sg.Button('', image_filename='icons\clear.png', key='x'),
             sg.Button('', image_filename=r'icons\btn_next.png', key='next')]
        ]

        return sg.Window('Repositórios', layout, element_justification='c',
                         finalize=True)

    @staticmethod
    def janela_repositorio_interfaces_graficas():
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Interfaces Gráficas', font=('Times New Roman', 20)),
             sg.Image(filename='icons\icon_interface.png')],
            [sg.Text('Este repositório contém interfaces gráficas de ' +
                     'códigos de outros repositórios, tornado-os ' +
                     'em algo mais visual e intuitivo.')],
            [sg.Text('Para as interfaces foi utilizado a biblioteca' +
                     ' PySimpleGUI, o que deixou-as muito bonitas')],
            [sg.Text('')],
            [sg.Text('Conteúdo:')],
            [sg.Image(filename='icons\interface1.png'),
             sg.Listbox(['Dicionário de tags do HTML',
                         'Gerador de senhas seguras'], size=(30, 1),
                        font=('Times New Roman', 12)),
             sg.Image(filename='icons\interface2.png')],
            [sg.Text('')],
            [sg.Button('', image_filename=r'icons\btn_icon_home.png',
                       key='home'),
             sg.Button('', image_filename=r'icons\btn_github.png', key='git'),
             sg.Button('', image_filename='icons\clear.png', key='x'),
             sg.Button('', image_filename=r'icons\btn_next.png', key='next')]
        ]

        return sg.Window('Interfaces Gráficas', layout,
                         element_justification='c', finalize=True)

    @staticmethod
    def janela_repositorio_dicionario_html():
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Dicionário HTML', font=('Times New Roman', 20)),
             sg.Image(filename='icons\icon_html.png')],
            [sg.Text('Este repositório é dedicado à Raphaela Ferraz.' +
                     'Contém um script em Python que é capaz de adicionar e ' +
                     'buscar tags do HTML5.')],
            [sg.Text('Tem o intuito de facilitar a busca por tags específicas'
                     + ', sendo alimentado conforme a Rapha vai'
                     + ' aprendendo')],
            [sg.Text('')],
            [sg.Text('Conteúdo:')],
            [sg.Image(filename='icons\icon_tags.png'),
             sg.Listbox(['Dicionário de tags do HTML'], size=(27, 1),
                        font=('Times New Roman', 12)),
             sg.Image(filename='icons\icon_tags.png')],
            [sg.Text('')],
            [sg.Button('', image_filename=r'icons\btn_icon_home.png',
                       key='home'),
             sg.Button('', image_filename=r'icons\btn_github.png', key='git'),
             sg.Button('', image_filename='icons\clear.png', key='x'),
             sg.Button('', image_filename=r'icons\btn_next.png', key='next')]
        ]

        return sg.Window('Dicionário HTML', layout, element_justification='c',
                         finalize=True)

    @staticmethod
    def janela_mais_repositorios():
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Mais Repositórios', font=('Times New Roman', 20)),
             sg.Image(filename='icons\icon_repo.png')],
            [sg.Text('Ainda há muitos outros repositórios no meu perfil!' +
                     ' Todos foram feitos em Python e abrangem ' +
                     'assuntos distintos e muito interessantes',
                     font=('Times New Roman', 13))],
            [sg.Text('')],
            [sg.Text('Automated Testings', size=(32, 1)),
             sg.Button('', image_filename=r'icons\btn_ok.png',
                       key='auto_tests')],
            [sg.Text('Validate', size=(32, 1)),
             sg.Button('', image_filename=r'icons\btn_ok.png',
                       key='validate')],
            [sg.Text('Automação Tabela Excel', size=(32, 1)),
             sg.Button('', image_filename=r'icons\btn_ok.png',
                       key='automacao_tabela')],
            [sg.Text('Extrator URL', size=(32, 1)),
             sg.Button('', image_filename=r'icons\btn_ok.png',
                       key='extrator')],
            [sg.Text('Playlist', size=(32, 1)),
             sg.Button('', image_filename=r'icons\btn_ok.png',
                       key='playlist')],
            [sg.Text('Análise Descritiva PNAD COVID-19', size=(32, 1)),
             sg.Button('', image_filename=r'icons\btn_ok.png',
                       key='analise_pnad')],
            [sg.Text('')],
            [sg.Button('', image_filename=r'icons\btn_icon_home.png',
                       key='home'),
             sg.Button('', image_filename=r'icons\btn_github.png', key='git'),
             sg.Button('', image_filename='icons\clear.png', key='x')]
        ]

        return sg.Window('Mais repositórios', layout, finalize=True,
                         element_justification='c')

    def chama_janelas(self):
        while True:
            janela, evento, valores = sg.read_all_windows()

            if evento == sg.WINDOW_CLOSED or evento == 'x':
                break

            elif evento == 'home':
                janela.hide()
                BoasVindas()

            elif janela == self.janela_cybersecurity:
                if evento == 'next':
                    self.janela_interfaces_graficas = self.janela_repositorio_interfaces_graficas()
                    self.janela_cybersecurity.hide()

                elif evento == 'git':
                    wb.open('https://github.com/VictorGM01/cybersecurity')

            elif janela == self.janela_interfaces_graficas:
                if evento == 'next':
                    self.janela_dicionario_html = self.janela_repositorio_dicionario_html()
                    self.janela_interfaces_graficas.hide()

                elif evento == 'git':
                    wb.open('https://github.com/VictorGM01/interfaces_graficas')

            elif janela == self.janela_dicionario_html:
                if evento == 'next':
                    self.janela_mais_repositorios = self.janela_mais_repositorios()
                    self.janela_dicionario_html.hide()

                elif evento == 'git':
                    wb.open('https://github.com/VictorGM01/DicionarioHtml')

            elif janela == self.janela_mais_repositorios:
                if evento == 'git':
                    wb.open('https://github.com/VictorGM01?tab=repositories')

                elif evento == 'auto_tests':
                    wb.open('https://github.com/VictorGM01/automated_testings')

                elif evento == 'validate':
                    wb.open('https://github.com/VictorGM01/validate')

                elif evento == 'automacao_tabela':
                    wb.open('https://github.com/VictorGM01/automacao_tabela_excel')

                elif evento == 'extrator':
                    wb.open('https://github.com/VictorGM01/ExtratorUrl')

                elif evento == 'playlist':
                    wb.open('https://github.com/VictorGM01/Playlist')

                elif evento == 'analise_pnad':
                    wb.open('https://github.com/VictorGM01/Analise_descritiva_PNAD_Covid19')


teste = BoasVindas()
