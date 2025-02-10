import tkinter as tk
from tkinter import ttk


family_relations= {
    "Father": {
        "Efik": "Ada",
        "Urhobo": "Baba",
        "Igbo": "Nna",
        "Hausa": "Baba",
        "Yoruba": "Bàbá"
    },
    "Mother": {
        "Efik": "Mma",
        "Urhobo": "Mama",
        "Igbo": "Nne",
        "Hausa": "Mama",
        "Yoruba": "Ìyá"
    },
    "Brother": {
        "Efik": "Ete",
        "Urhobo": "Uvwie",
        "Igbo": "Nwanne",
        "Hausa": "Yaya",
        "Yoruba": "Ẹgbọ́n"
    },
    "Sister": {
        "Efik": "Eka",
        "Urhobo": "Erhi",
        "Igbo": "Nwanyi",
        "Hausa": "'Yar",
        "Yoruba": "Ẹgbọ́n obìnrin"
    },
    "Siblings": {
        "Efik": "Idung",
        "Urhobo": "Evwie",
        "Igbo": "Ụmụnne",
        "Hausa": "Yara",
        "Yoruba": "Ẹgbọ́n"
    },
    "Aunt": {
        "Efik": "Inyang",
        "Urhobo": "Oghene",
        "Igbo": "Nne",
        "Hausa": "Uwa",
        "Yoruba": "Ìyá agbà"
    },
    "Uncle": {
        "Efik": "Ekpe",
        "Urhobo": "Ovie",
        "Igbo": "Nna",
        "Hausa": "Uncle",
        "Yoruba": "Bàbá agbà"
    },
    "Cousin": {
        "Efik": "Ete",
        "Urhobo": "Uvwie",
        "Igbo": "Nwanne",
        "Hausa": "Dan'uwa",
        "Yoruba": "Ọmọ̀ ẹgbọ́n"
    },
"Nephew": {
        "Efik": "Ete",
        "Urhobo": "Uvwie",
        "Igbo": "Nwana",
        "Hausa": "Dan'uwa",
        "Yoruba": "Ọmọ̀kùnrin"
    },
    "Niece": {
        "Efik": "Eka",
        "Urhobo": "Erhi",
        "Igbo": "Nwada",
        "Hausa": "'Yar'uwa",
        "Yoruba": "Ọmọ̀bìnrin"
    },
    "Grandfather": {
        "Efik": "Ada Oro",
        "Urhobo": "Baba Oro",
        "Igbo": "Nna Nna",
        "Hausa": "Baba Baba",
        "Yoruba": "Bàbá bàbá"
    },
    "Grandmother": {
        "Efik": "Mma Oro",
        "Urhobo": "Mama Oro",
        "Igbo": "Nne Nne",
        "Hausa": "Mama Mama",
        "Yoruba": "Ìyá ìyá"
    },
}


def translate():
    relation = relation_var.get()
    language = language_var.get()
    translation = family_relations[relation][language]
    result_label.config(text=f"{relation} in {language} is {translation}")

root = tk.Tk()
root.title("Family Relations Translator")

relation_var = tk.StringVar()
relation_var.set("Father")

relation_label = tk.Label(root, text="Select a relation:")
relation_label.pack()

relation_option = tk.OptionMenu(root, relation_var, *family_relations.keys())
relation_option.pack()

language_var = tk.StringVar()
language_var.set("Yoruba")

language_label = tk.Label(root, text="Select a language:")
language_label.pack()

language_option = tk.OptionMenu(root, language_var, *family_relations["Father"].keys())
language_option.pack()

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
