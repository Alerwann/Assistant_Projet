from tkinter import  ttk, Label, Frame


class ProgressBarMixin:

    def finish_progressbar(self, nom):
        self.progressbars_frame[nom].destroy()
        del self.progressbars_frame[nom]

    def create_progressBar(self, nom, duree_seconde):
        """création de la barre de progrssion """
        duree_minute = duree_seconde//60

        frame_timer = Frame(self.zone_progressbars)
        frame_timer.pack(pady=5)

        label = Label(frame_timer, text=f"Avancement de {nom}")
        label.pack()

        progress = ttk.Progressbar(frame_timer,  length=300)
        progress.pack(pady=10)
        progress.config(value=-1, maximum=duree_minute)
        progress.start(60000)

        self.progressbars_frame[nom] = frame_timer

        duree_milliseconde = int(duree_seconde * 1000)
        self.fenetre.after(duree_milliseconde, lambda:self.finish_progressbar(nom))
