from kivymd.app import MDApp
from kivy.lang.builder import Builder
import asynckivy as ak
import requests


class TestApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def downloading(self, url):
        img_bytes = requests.get(url).content
        name = url.split("/")[3].split("-")[0] + "_" + \
            url.split("/")[3].split("-")[1] + ".jpg"
        with open(name, 'wb') as f_obj:
            f_obj.write(img_bytes)

    def on_press(self):
        async def some_task():
            button = self.root.ids.down_button
            url = self.root.ids.input
            # label = self.root.ids.label
            spinner = self.root.ids.spinner

            # label.text = "Downloading"
            spinner.active = True
            await ak.run_in_thread(lambda: self.downloading(url.text))
            # label.text = f'''{url.text.split("/")[3].split("-")[0] + "_" + url.text.split("/")[3].split("-")[1] + ".jpg"} was downloaded'''
            spinner.active = False

        ak.start(some_task())


if __name__ == '__main__':
    TestApp().run()
