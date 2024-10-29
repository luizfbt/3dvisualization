import os
import pdb
import subprocess
import flet as ft
import time

"""This script provides an interface for the user to select the desired demo.
Uses the Flet library from Python, https://flet.dev/.
For information on installation dependencies, see README.md."""

this_path = os.path.abspath(os.path.dirname(__file__))
demos_path = os.path.join(this_path, 'demos')
python_folder = os.path.join(this_path, 'venv', 'Scripts')
python_exe = os.path.join(python_folder, 'python.exe')
jupyterlab_exe = os.path.join(python_folder, 'jupyter-lab.exe')
if not os.path.exists(python_exe):
    print(f"The 'python.exe' file not found at: {python_folder}")
    exit(1)


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "3D Visualization Script Explorer"
        self.page.scroll = ft.ScrollMode.AUTO
        self.actual_path = demos_path
        self.can_execute = True
        self.update_page()


    def list_files_and_dirs(self):
        """Lists files and directories in a specified path."""
        if self.actual_path == demos_path:
            items = []
        else:
            path = os.path.split(self.actual_path)[0]
            items = [
                ft.Stack(
                    [
                        ft.Image(
                            src='images/yellow_folder.png',
                            fit=ft.ImageFit.FILL
                        ),
                        ft.Container(
                            content=ft.Icon(
                                name=ft.icons.ARROW_UPWARD,
                                color=ft.colors.BLACK),
                            alignment=ft.alignment.center,
                            on_click=lambda e, p=path: self.on_item_click(e, p),
                        )
                    ],
                    width=100,
                    height=100,
                )
            ]
        
        for item in os.listdir(self.actual_path):
            full_path = os.path.join(self.actual_path, item)
            if os.path.isdir(full_path):
                src = 'images/yellow_folder.png'
            else:
                src = 'images/blue_file.png'

            items.append(
                ft.Stack(
                    [
                        ft.Image(
                            src=src,
                            fit=ft.ImageFit.FILL
                        ),
                        ft.Container(
                            content=ft.Text(
                                item,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.BLACK,
                                size=12,
                                weight=ft.FontWeight.BOLD,
                            ),
                            alignment=ft.alignment.center,
                            on_click=lambda e, p=full_path: self.on_item_click(e, p),
                        ),
                    ],
                    width=100,
                    height=100,
                )
            )
        return items


    def on_item_click(self, e: ft.ControlEvent, path: str):
        """Callback when an item (folder or file) is clicked."""
        if not self.can_execute:
            return
        
        if os.path.isdir(path):
            # Refreshes the view to the contents of the folder
            self.actual_path = path
            self.page.controls.pop()
            self.update_page()
        
        elif path.endswith(".py"):
            # Run the Python script
            try:
                self.change_container_bgcolor(e.control)
                subprocess.run([python_exe, path], check=True)
            except Exception as e:
                print(f"Error when running the script: {e}")
        
        elif path.endswith(".ipynb"):
            # Run the Jupyter Lab and opens the script
            try:
                self.change_container_bgcolor(e.control)
                subprocess.run([jupyterlab_exe, path], check=True)
            except Exception as e:
                print(f"Error when running the Jupyter Lab: {e}")
            
        elif path.endswith(".md") or path.endswith(".rst") or path.endswith(".txt"):
            self.show_doc(path)

    
    def change_container_bgcolor(self, control: ft.Container):
        self.can_execute = False
        control.border=ft.border.all(5, ft.colors.GREEN)
        control.update()
        time.sleep(2.0)
        control.border = None
        control.update()
        self.can_execute = True



    def update_page(self):
        """Builds all controls in the page.
        """
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text(f"Dir: {self.actual_path}"),
                    ft.GridView(
                        expand=1,
                        runs_count=5,
                        max_extent=150,
                        child_aspect_ratio=1.25,
                        spacing=5,
                        run_spacing=5,
                        controls=self.list_files_and_dirs(),
                    ),
                ]
            )
        )
        self.page.update()
    

    def show_doc(self, path: str):
        with open(path, mode='r', encoding='utf-8') as file_ref:
            markdown = file_ref.read()

        filename = os.path.split(path)[1]
        self.dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                f"{filename}",
                theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM
            )
        )

        if path.endswith(".txt"):
            md = ft.Text(markdown)
        else:
            md = ft.Markdown(
                value=markdown,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                on_tap_link=lambda e: self.page.launch_url(e.data),
            )

        self.dlg.content = ft.Column(
            controls=[md],
            scroll=ft.ScrollMode.ADAPTIVE,
        )

        self.dlg.actions=[
            ft.TextButton("Close", on_click=self.on_close_doc)
        ]

        self.page.open(self.dlg)
    

    def on_close_doc(self, e: ft.ControlEvent):
        self.page.close(self.dlg)


ft.app(target=App, assets_dir="assets")
