import flet as ft 
from fonction import Permut, Combi


def main(page: ft.Page):

    def affresult(ensemble:list):
        pass

    # Fonction de remise a zero
    def reset(e):
        nb_ele.value = None
        num.value = None
        repetition.value = False
        ope.value = "Combinaison"
        reponse.value = None 
        page.update()

    # fonction de calcul
    def calcul(e):
        nb = int(nb_ele.value)
        nu = int(num.value)
        repet = repetition.value
        op = ope.value

        if op == 'Combinaison':
            val = Combi(nb, nu, repet)
            if not val:
                error_dialog.open = True
                page.update()
            else:
                reponse.value = val
                page.update()
        else:
            val = Permut(nb, nu, repet)
            if not val:
                error_dialog.open = True
                page.update()
            else:
                reponse.value = val
                page.update()

        page.update()

    # Fonction d'affichage de l'erreur
    def error_close(e):
        error_dialog.open = False
        page.update()

    def ok(e):
        nb_ele.disabled = True
        page.update()

    # Variable du formulaire
    text = ft.Text("Cette applications a pour objectif de calculer les r_combinason et les r_arrangement avec ou sans repetitions.", italic=True, theme_style=ft.TextThemeStyle.BODY_SMALL)
    ensem = ft.TextField(hint_text="ensemble(1,2,3,...,)", on_change=ok)
    nb_ele = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, hint_text="cardinal", expand=1)
    num = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, hint_text="r_uplet", expand=1)
    ope = ft.Dropdown(value="Combinaison",options=[
            ft.dropdown.Option("Combinaison"),
            ft.dropdown.Option("Permutation")
        ],
    )
    reponse = ft.TextField(hint_text="resultat", disabled=True, multiline=True)
    repetition = ft.Checkbox(value=False, label="repetition")

    # Affichage de l'erreur
    error_dialog = ft.AlertDialog(
        title= ft.Text("error"),
        content=ft.Text("Une erreur de donnees ou de syntaxe c'est produit! veillez verifier vos donnees"),
        actions= [
            ft.FilledButton(text="ok", on_click=error_close),
        ],
        open=False,
    )

    # affichage pour la section information
    info_view = ft.Column(
        controls=[
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[ft.Text("info", theme_style=ft.TextThemeStyle.TITLE_MEDIUM), ft.Icon(name=ft.icons.INFO)]),
            text,
        ],
    )
    
    # Affichage pour l'entete
    head = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(value="Devoir ensemble", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ft.Icon(name=ft.icons.BOOK_SHARP),
        ]
    )

    # Toute l'interface de calcul
    ope_view = ft.Column(
        spacing=30,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        controls=[
            ensem,
            ft.Row(
                spacing= 10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[nb_ele, num],
            ),
            ope,
            ft.Row(
                vertical_alignment= ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(text="Calculer", icon=ft.icons.CALCULATE, expand=True, on_click=calcul),
                    repetition,
                ]
            ),
            reponse
        ]
    )
    #Fin interface de calcul


    # Vue generale ou on affiche toute les autres views
    view = ft.Column(
        adaptive=True,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        controls=[
            head,
            ft.Divider(),
            error_dialog,
            ft.Column(
                width = 600,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                controls=[
                    info_view,
                    ft.Divider(),
                    ope_view,
                    ft.Row(
                        expand=1,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(expand=1),
                            ft.FloatingActionButton(icon=ft.icons.RESTART_ALT, on_click=reset),
                        ],
                    ),
                ],
            ),
            
        ],
    )
    # Fin


    page.add(view)
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

ft.app(main)