import webbrowser as wb
import PySimpleGUI as sg


class BoasVindas:

    def __init__(self):
        self.janela_inicial()
        self.loop_entre_as_janelas()

    def janela_inicial(self):
        sg.theme('DarkTeal9')
        layout = [
            [sg.Text('Seja bem-vindx ao meu perfil',
             font=('Helvetica', 25), justification='c')],
            [sg.Text('Detalhar Repositórios', size=(25, 1)),
             sg.Checkbox('', default=False, key='repositorios')],
            [sg.Text('Sobre mim - Perfil', size=(25, 1)),
             sg.Checkbox('', default=False, key='perfil')],
            [sg.Text('Linguagens mais usadas', size=(25, 1)),
             sg.Checkbox('', default=False, key='linguagens')],
            [sg.Text('Assuntos', size=(25, 1)),
             sg.Checkbox('', default=False, key='assuntos')],
            [sg.Button('IR', key='ok'),
             sg.Button('Cancelar', key='x')]
        ]

        return sg.Window('Boas vindas', layout, finalize=True)

    def janela_repositorios(self):
        pass

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
