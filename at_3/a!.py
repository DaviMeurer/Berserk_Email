import flet as ft

def main(page):
    def mudar_tela(route):  # definindo rotas
        page.views.clear()  # limpando telas anteriores

        # rota da página inicial
        if page.route == "/tela1":
            page.views.append(
                ft.View(
                    controls=[  # Definindo os controles da tela
                        ft.Text("Tela 1", size=30),
                        ft.ElevatedButton("Ir para tela 2", on_click=lambda e: page.go("/tela2"))
                    ]
                )
            )
        elif page.route == "/tela2":
            page.views.append(
                ft.View(
                    controls=[  # Definindo os controles da tela
                        ft.Text("Tela 2", size=38),
                        ft.ElevatedButton("Voltar para a tela 1", on_click=lambda e: page.go("/tela1"))
                    ]
                )
            )
        page.update()  # Atualizando a página para refletir as mudanças

    page.on_route_change = mudar_tela
    page.go("/tela1")  # Inicia na tela 1

ft.app(target=main)
