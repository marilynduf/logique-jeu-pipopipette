# -*- coding: utf-8 -*-

from planche import Planche
from joueur import JoueurOrdinateur, JoueurHumain


class PartiePipopipette:
    def __init__(self, nom_fichier=None):
        """
        Méthode d'initialisation d'une partie de pipopipette.
        """
        self.planche = Planche()

        self.gagnant_partie = None
        self.partie_nulle = False

        if nom_fichier is not None:
            self.charger(nom_fichier)
        else:
            self.initialiser_joueurs()

    def initialiser_joueurs(self):
        """
        ÉTAPE 4

        On initialise ici quatre attributs : joueur_rouge,
        joueur_bleu, joueur_courant et couleur_joueur_courant.

        Pour créer les objets joueur_rouge et joueur_bleu, faites
        appel à creer_joueur().

        joueur_courant est initialisé par défaut au joueur_rouge
        et couleur_joueur_courant est initialisée à 'rouge'.

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def creer_joueur(self, couleur):
        """
        ÉTAPE 4

        Demande à l'usager quel type de joueur ('Humain' ou
        'Ordinateur') il désire pour le joueur de la couleur
        en entrée.

        Tant que l'entrée n'est pas valide, on continue de
        demander à l'utilisateur.

        Faites appel à self.creer_joueur_selon_type() pour créer
        le joueur lorsque vous aurez un type valide.

        Args :
            couleur (str): la couleur pour laquelle on veut le type
                de joueur.

        Returns :
            Joueur : Un objet Joueur, de type JoueurHumain si l'usager a
                entré 'Humain', JoueurOrdinateur s'il a entré
                'Ordinateur'.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def creer_joueur_selon_type(self, type_joueur, couleur):
        """
        ÉTAPE 4

        Crée l'objet Joueur approprié, selon le type passé en
        paramètre.

        Pour créer les objets, vous n'avez qu'à faire appel à
        leurs constructeurs, c'est-à-dire à
        JoueurHumain(couleur), par exemple.

        Args :
            type (str): le type de joueur, 'Ordinateur' ou 'Humain'
            couleur (str): la couleur du pion joué par le joueur,
                'rouge' ou 'bleu'.

        Returns :
            Joueur: Un objet JoueurHumain si le type est 'Humain',
                JoueurOrdinateur sinon.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def jouer(self):
        """
        ÉTAPE 5

        Méthode représentant la boucle principale de jeu.

        On commence par faire afficher un message indiquant le début
        de la partie ainsi que l'état de départ de la planche.

        Ensuite on fonctionne comme une boucle. Pour chaque
        itération, on joue un tour et si la partie est terminée,
        on quitte la boucle.

        Quand on sort de la boucle principale, on fait afficher le
        message de fin de la partie.

        Utilisez les fonctions partie_terminee(), jouer_tour() et
        message_fin_partie() pour vous faciliter la tâche.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def jouer_tour(self):
        """
        ÉTAPE 5

        Cette méthode commence par afficher à quel joueur c'est
        le tour de jouer et faire imprimer l'état de la planche avec
        print(self.planche).

        On va ensuite chercher le coup choisi par le joueur courant
        avec la méthode choisir_coup() de Joueur en lui passant la
        planche de jeu courante (self.planche). Tant que le coup choisi
        par un joueur n'est pas valide, on affiche la raison de
        l'invalidité du coup et on redemande au joueur de choisir un
        coup. Voir les commentaires de la méthode valider_coup() de Planche
        pour plus de détails.

        On finit par jouer le coup (validé) avec la méthode self.jouer_coup().

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def jouer_coup(self, coup):
        """
        ÉTAPE 5

        Joue un coup sur la planche, fait la mise à jour de l'état
        des boîtes et change de joueur au besoin (si aucune boîte
        n'a été remplie en jouant le coup).

        Faites appel aux méthodes jouer_coup() et maj_boites() de
        Planche ainsi qu'à self.changer_joueur()

        Args:
            coup (int, int, str): L'index de la ligne à jouer

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def partie_terminee(self):
        """
        ÉTAPE 5

        Méthode vérifiant si la partie est terminée.

        Pour savoir si la planche de jeu est pleine, on peut
        directement faire appel à self.planche.est_pleine(). Si
        la planche est pleine, c'est que la partie est terminée.
        On fait donc imprimer un message indiquant la fin de la
        partie ainsi que l'état final de planche.

        Il nous reste maintenant à savoir qui est le gagnant de
        la partie. Pour obtenir le nombre de boîtes remplies par chacun
        des joueurs, faites appel à la fonction bilan_boites()
        de l'attribut self.planche. On assigne la couleur du
        joueur gagnant (celui avec le plus de boîtes) à l'attribut
        self.gagnant_partie.

        Returns :
            True si la partie est terminée, False sinon

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def changer_joueur(self):
        """
        ÉTAPE 5

        En fonction de la couleur du joueur courant, met à
        jour les attributs joueur_courant et couleur_joueur_courant.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def message_fin_partie(self):
        """
        ÉTAPE 5

        Méthode qui gère le comportement de fin de partie.

        On retourne un message approprié pour féliciter le gagnant.
        Le joueur gagnant est contenu dans l'attribut
        self.gagnant_partie.

        Returns:
            str: le message de félicitations du gagnant de la partie.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def sauvegarder(self, nom_fichier):
        """
        ÉTAPE 6

        Sauvegarde une partie dans un fichier. Le fichier
        contiendra:
        - Une ligne indiquant la couleur du joueur courant.
        - Une ligne contenant le type du joueur rouge.
        - Une ligne contenant le type du joueur bleu.
        - Le reste des lignes correspondant aux lignes et aux boîtes. Voir la
          méthode convertir_en_chaine() de la planche pour le
          format.

        Faites appel à la fonction obtenir_type_joueur() de
        la classe Joueur pour savoir le type d'un Joueur.

        Args :
            nom_fichier, le string du nom du fichier où sauvegarder.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass

    def charger(self, nom_fichier):
        """
        Charge une partie à partir d'un fichier. Le fichier
        a le même format que la méthode de sauvegarde.

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        Args:
            nom_fichier (str): Le du nom du fichier à charger.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        pass
