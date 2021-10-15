import webbrowser as wb
import PySimpleGUI as sg


class BoasVindas:

    def __init__(self):
        self.janela_repositorio_cybersecurity()
        self.loop_entre_as_janelas()

    @staticmethod
    def janela_inicial():
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
            [sg.Button('', image_filename=r'icons\btn_ok.png', key='ok'),
             sg.Button('', image_filename='icons\clear.png', key='x'),
             sg.Button('', image_filename='icons\icon_help.png', key='ajuda')]
        ]

        return sg.Window('Home', layout,
                         element_justification='c', finalize=True)

    @staticmethod
    def janela_repositorio_cybersecurity():
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Cybersecurity', font=('Times New Roman', 20))],
            [sg.Text('Este repositório tem como objetivo relacionar a ' +
                     'linguagem de programação Python com a ' +
                     'Segurança Cibernética')],
            [sg.Text('Contém scripts em Python que visam aplicar os conceitos'
                     + ' de cibersegurança por meio da programação')],
            [sg.Text('Conteúdo:')],
            [sg.Listbox(['Gerador de senha', 'Gerador de Hash',
                         'Comparador de Hashes', 'Criptografador de arquivos',
                         'Descriptografador de arquivos',
                         'Criptografador da Cifra de César',
                         'Descriptografador da Cifra de César'], size=(35, 1),
                        font=('Times New Roman', 12))],
            [sg.Button('', image_filename=r'icons\btn_icon_home.png',
                       key='home'),
             sg.Button('', image_filename=r'icons\btn_github.png', key='git'),
             sg.Button('', image_filename='icons\clear.png', key='x')]
        ]

        return sg.Window('Repositórios', layout, element_justification='c',
                         finalize=True)

    def janela_perfil(self):
        pass

    def janela_assuntos(self):
        pass

    def loop_entre_as_janelas(self):
        while True:
            janela, evento, valores = sg.read_all_windows()

            if evento == sg.WINDOW_CLOSED or evento == 'x':
                break


teste = BoasVindas()
