# -*- coding: utf-8 -*-

from pipopipette.planche import Planche
from pipopipette.joueur import JoueurOrdinateur, JoueurHumain


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

        On initialise ici quatre attributs :
        self.joueur_rouge,
        self.joueur_bleu,
        self.joueur_courant
        self.couleur_joueur_courant.

        Pour créer les attributs self.joueur_rouge et self.joueur_bleu, faites
        appel à self.creer_joueur().

        self.joueur_courant est initialisé par défaut au self.joueur_rouge
        et self.couleur_joueur_courant est initialisée à 'rouge'.

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        TODO: Vous devez compléter le corps de cette fonction.
        """

        self.joueur_rouge = self.creer_joueur('rouge')  # crée le joueur rouge
        self.joueur_bleu = self.creer_joueur('bleu')  # crée le joueur bleu
        self.joueur_courant = self.joueur_rouge  # assigne le joueur rouge au joueur courant
        self.couleur_joueur_courant = 'rouge'  # assigne la couleur rouge au joueur courant

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

        # type_joueur = ''
        #
        # # crée le type de joueur pour la couleur rouge
        # if couleur == 'rouge':
        #     while type_joueur != 'Humain' and type_joueur != 'Ordinateur':
        #         type_joueur = input('Quel type de joueur désirez-vous pour la couleur rouge? Entrez Humain ou Ordinateur')
        #
        # # crée le type de joueur pour la couleur bleu
        # if couleur == 'bleu':
        #     while type_joueur != 'Humain' and type_joueur != 'Ordinateur':
        #         type_joueur = input(
        #             'Quel type de joueur désirez-vous pour la couleur bleu? Entrez Humain ou Ordinateur')

        joueur = self.creer_joueur_selon_type('Humain', couleur)

        return joueur

    def creer_joueur_selon_type(self, type_joueur, couleur):
        """
        ÉTAPE 4

        Crée l'objet Joueur approprié, selon le type passé en
        paramètre.

        Pour créer les objets, vous n'avez qu'à faire appel à
        leurs constructeurs, c'est-à-dire à
        JoueurHumain(couleur), par exemple.

        Args :
            type_joueur (str): le type de joueur, 'Ordinateur' ou 'Humain'
            couleur (str): la couleur du pion joué par le joueur,
                'rouge' ou 'bleu'.

        Returns :
            Joueur: Un objet JoueurHumain si le type est 'Humain',
                JoueurOrdinateur sinon.

        TODO: Vous devez compléter le corps de cette fonction.
        """

        if type_joueur == 'Humain':
            joueur = JoueurHumain(couleur)  # crée le type de joueur Humain

        else:
            joueur = JoueurOrdinateur(couleur)  # crée le type de joueur Ordinateur

        return joueur

    def jouer(self):
        """
        ÉTAPE 5

        Méthode représentant la boucle principale de jeu.

        On commence par faire afficher un message indiquant le début
        de la partie ainsi que l'état de départ de la planche.

        Ensuite on fonctionne avec une boucle. Pour chaque
        itération, on joue un tour et si la partie est terminée,
        on quitte la boucle.

        Quand on sort de la boucle principale, on fait afficher le
        message de fin de la partie.()

        Utilisez les fonctions self.partie_terminee(), self.jouer_tour() et
        self.message_fin_partie() pour vous faciliter la tâche.

        TODO: Vous devez compléter le corps de cette fonction.
        """

    def jouer_tour(self, coup):
        """
        ÉTAPE 5

        Cette méthode commence par afficher à quel joueur c'est
        le tour de jouer.

        On va ensuite chercher le coup choisi par le joueur courant
        avec la méthode choisir_coup() de Joueur en lui passant la
        planche de jeu courante (self.planche). Tant que le coup choisi
        par un joueur n'est pas valide, on affiche la raison de
        l'invalidité du coup et on redemande au joueur de choisir un
        coup. Voir les commentaires de la méthode valider_coup() de Planche
        pour plus de détails.

        On finit par jouer le coup (validé) avec la méthode self.jouer_coup().
        et faire imprimer l'état de la planche avec print(self.planche).

        TODO: Vous devez compléter le corps de cette fonction.
        """

        self.jouer_coup(coup)  # applique le coup

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
        coup_valide = self.planche.valider_coup(coup)
        if coup_valide:
            self.planche.jouer_coup(coup, self.joueur_courant.couleur)
            couleur = self.joueur_courant.couleur

            self.planche.jouer_coup(coup, couleur)  # applique le coup du joueur courant sur la planche

            maj_boite = self.planche.maj_boites()  # fait la mise è jour des boites

            # change de joueur si aucune boite n'a été remplie
            if not maj_boite:
                self.changer_joueur()

    def partie_terminee(self):
        """
        ÉTAPE 5

        Méthode vérifiant si la partie est terminée.

        Pour savoir si la planche de jeu est pleine, on peut
        directement faire appel à self.planche.est_pleine(). Si
        la planche est pleine, c'est que la partie est terminée.

        Il faut alors savoir qui est le gagnant de la partie.
        Pour obtenir le nombre de boîtes remplies par chacun
        des joueurs, faites appel à la fonction bilan_boites()
        de l'attribut self.planche. On assigne la couleur du
        joueur gagnant (celui avec le plus de boîtes) à l'attribut
        self.gagnant_partie.

        Returns :
            True si la partie est terminée, False sinon

        TODO: Vous devez compléter le corps de cette fonction.
        """
        planche_pleine = self.planche.est_pleine()

        # calcul le nombre de boite remplie par chacun des joueurs
        if planche_pleine:
            bilan_boite = self.planche.bilan_boites()
            nb_boite_bleu = bilan_boite[0]
            nb_boite_rouge = bilan_boite[1]

            # détermine le joueur ganant
            if nb_boite_rouge > nb_boite_bleu:
                self.gagnant_partie = self.joueur_rouge.couleur

            else:
                self.gagnant_partie = self.joueur_bleu.couleur

            return True

        return False

    def changer_joueur(self):
        """
        ÉTAPE 5

        En fonction de la couleur du joueur courant, met à
        jour les attributs joueur_courant et couleur_joueur_courant.

        TODO: Vous devez compléter le corps de cette fonction.
        """

        if self.joueur_courant.couleur == 'rouge':
            self.joueur_courant = self.joueur_bleu
            self.couleur_joueur_courant = 'bleu'
        else:
            self.joueur_courant = self.joueur_rouge
            self.couleur_joueur_courant = 'rouge'

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
        message_fin_partie = 'Fin de la partie.\n Le gagnant de la partie est le joueur {} !'.format(self.gagnant_partie)

        return message_fin_partie

    # def sauvegarder(self, nom_fichier):
    #     """
    #     ÉTAPE 6
    #
    #     Sauvegarde une partie dans un fichier. Le fichier
    #     contiendra:
    #     - Une ligne indiquant la couleur du joueur courant.
    #     - Une ligne contenant le type du joueur rouge.
    #     - Une ligne contenant le type du joueur bleu.
    #     - Le reste des lignes correspondant aux lignes et aux boîtes. Voir la
    #       méthode convertir_en_chaine() de la planche pour le
    #       format.
    #
    #     Faites appel à la fonction obtenir_type_joueur() de
    #     la classe Joueur pour savoir le type d'un Joueur.
    #
    #     Args :
    #         nom_fichier, le string du nom du fichier où sauvegarder.
    #
    #     TODO: Vous devez compléter le corps de cette fonction.
    #     """
    #
    #     couleur_joueur_courant = self.joueur_courant.couleur
    #     type_joueur_rouge = self.joueur_rouge.obtenir_type_joueur()
    #     type_joueur_bleu = self.joueur_bleu.obtenir_type_joueur()
    #     lignes_et_boites_jouees = self.planche.convertir_en_chaine()
    #
    #     info_partie_en_cour = couleur_joueur_courant + '\n' + type_joueur_bleu + '\n' + type_joueur_rouge + '\n' + lignes_et_boites_jouees
    #
    #     fichier_destination = open('partie_sauvegardee.txt', 'w')
    #     fichier_destination.write(info_partie_en_cour)
    #     fichier_destination.close()
    #
    #     return nom_fichier, 'partie_sauvegardee_2.txt'

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

        fichier_source = open(nom_fichier)
        info_lignes = []

        for ligne in fichier_source:
            ligne = ligne.strip()
            info_lignes.append(ligne)

        # prend les 3 premières lignes de la liste
        couleur = info_lignes[0]
        type_joueur_rouge = info_lignes[1]
        type_joueur_bleu = info_lignes[2]

        for info in info_lignes[3:]:
            ligne = int(info[0])
            colonne = int(info[2])
            attribut_ligne = str(info[4])

            if attribut_ligne == 'H' or attribut_ligne == 'V':
                self.planche.lignes[(ligne, colonne, attribut_ligne)].jouee = True
            else:
                attribut_boite = str(info[4:])
                self.planche.boites[(ligne, colonne)].pleine = True
                self.planche.boites[(ligne, colonne)].couleur = attribut_boite

        self.joueur_rouge = self.creer_joueur_selon_type(type_joueur_rouge, couleur)
        self.joueur_bleu = self.creer_joueur_selon_type(type_joueur_bleu, 'bleu')
        self.joueur_courant = self.joueur_rouge
        self.joueur_courant.couleur = couleur

        fichier_source.close()
