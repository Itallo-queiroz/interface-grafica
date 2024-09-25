import flet as ft

def main(page: ft.Page):
    page.title = "Hello World!"
    page.scroll = "adaptive"

    # declaração de variavel
    nome = ft.TextField(label='Nome')

    page.add(
        ft.Text('Hello World', size=35, color='blue', weight='bold'),
    nome,
    ft.TextButton('clique aqui')
                     
                     
    )

    page.update()

ft.app(main)








