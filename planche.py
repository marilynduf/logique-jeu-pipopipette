# -*- coding: utf-8 -*-

from pipopipette.ligne import Ligne
from pipopipette.boite import Boite
from pipopipette.exceptions import ErreurPositionCoup
from tkinter import messagebox

class Planche:
    """
    Classe représentant la planche de jeu de Pipopipette.

    Le système de position de la planche fonctionne comme suit:

        - Les points sont représentés par un tuple (ligne, colonne)
          respectant l'indexage habituel d'une matrice; le point
          en haut à gauche est représenté par le tuple (0, 0) alors
          que le point en bas à droite est représenté par le tuple
          (Planche.N_BOITES_H, Planche.N_BOITES_V).

        - Les boîtes sont représentées par l'index du point se situant
          dans leur coin supérieur gauche. Cela veut donc dire que la
          boîte du coin en haut à gauche est représentée par le tuple
          (0, 0) alors que celle en bas à droite est représentée par
          le tuple (Planche.N_BOITES_H - 1, Planche.N_BOITES_V - 1).
          Remarquez bien ici les -1: ils sont présents pour la dernière
          boîte mais pas pour le dernier point car il y a plus de points
          que de boîtes dans une partie de pipopipette.

        - Il existe deux types de lignes: les lignes verticales et
          horizontales. On considèrera qu'une ligne est représentée
          notamment par une chaîne de caractères 'orientation', laquelle
          vaudra 'H' pour une ligne horizontale et 'V' pour une ligne
          verticale. Enfin, une ligne est aussi reliée à l'index (ligne,
          colonne) d'un point de la planche. Pour une ligne verticale,
          le point de connexion est celui du haut de la ligne, alors que
          pour une ligne horizontale, il s'agit du point à gauche. Ainsi,
          chaque ligne se voit attribuer un tuple (ligne, colonne, orientation)
          unique.
    """
    # Attributs globaux de la classe Planche.
    # Vous pouvez leur accéder avec Planche.N_BOITES_H par exemple.
    # Noter que dans le vidéo explicatif, self.N_COLONNES représentait
    # self.N_BOITES_V et ainsi de suite.

    N_BOITES_V = 3
    N_BOITES_H = 3

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle planche.
        """
        self.initialisation_par_defaut()
        self.position_dernier_coup = None
        self.couleur_dernier_coup = None

    def initialisation_par_defaut(self):
        """
        Méthode initialisant les dictionnaires de lignes et de boîtes
        de la planche.
        """
        self.initialiser_lignes()
        self.initialiser_boites()

    def initialiser_lignes(self):
        """
        ÉTAPE 1

        Méthode d'initialisation des lignes contenues dans self.lignes.
        Cet attribut permettra d'accéder à une ligne de la planche à partir
        de son index comme suit :

            self.lignes[(ligne, colonne, orientation)]

        On débute par créer un dictionnaire vide de lignes dans l'attribut
        self.lignes. On crée et on ajoute ensuite les lignes à self.lignes
        au bon index pour chacun des trois types de ligne suivants :

        - La ligne verticale à droite : Toutes les lignes verticales qui ont
          comme colonne la valeur Planche.N_BOITES_V. Notez qu'il y en aura
          précisément Planche.N_BOITES_H.

        - La ligne horizontale du bas : Toutes les lignes horizontales qui ont
          comme index de ligne la valeur Planche.N_BOITES_H. Notez qu'il y en aura
          précisément Planche.N_BOITES_V.

        - Les lignes dites 'de base' : Toutes les lignes horizontales et verticales
          qui ne sont pas dans la ligne du bas ni celle de droite (cas plus haut).
          Notez qu'il y en aura précisément Planche.N_BOITES_V * Planche.N_BOITES_H.

        L'index d'une ligne (sa clé dans self.lignes) doit correspondre à un tuple
        (ligne, colonne, orientation) tel que décrit dans les commentaires au haut
        de cette classe. Pour créer un objet Ligne, faites simplement appel au
        constructeur Ligne().

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        TODO: Vous devez compléter le corps de cette fonction.
        """

        self.lignes = {}

        for index_ligne_verticale in range(self.N_BOITES_V):  # Lignes horizontales à droite
            self.lignes[(index_ligne_verticale, self.N_BOITES_H, 'V')] = Ligne()

        for index_ligne_horizontale in range(self.N_BOITES_H):  # Lignes horizontales du bas
            self.lignes[(self.N_BOITES_V, index_ligne_horizontale, 'H')] = Ligne()

        for index_ligne_horizontale in range(self.N_BOITES_H): # lignes de base
            for index_ligne_verticale in range(self.N_BOITES_V):
                for orientation in ['H', 'V']:
                    self.lignes[(index_ligne_verticale, index_ligne_horizontale, orientation)] = Ligne()

    def initialiser_boites(self):
        """
        ÉTAPE 1

        Méthode d'initialisation des boîtes contenues dans self.boites.
        Cet attribut permet d'accéder à une boîte de la planche à partir
        de son index comme suit :

            self.boites[(ligne, colonne)]

        On débute par créer un dictionnaire vide de boîtes dans l'attribut
        self.boites. On crée et on ajoute ensuite les boîtes à self.boites
        au bon index pour toutes les boîtes de la planche. Notez qu'il y en
        aura précisément Planche.N_BOITES_V * Planche.N_BOITES_H.

        L'index d'une boîte (sa clé dans self.boites) doit correspondre à un tuple
        (ligne, colonne) tel que décrit dans les commentaires au haut de cette
        classe. Pour créer un objet Boite, faites simplement appel au
        constructeur Boite().

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        TODO: Vous devez compléter le corps de cette fonction.
        """
        # Créer un dictionnaire de boites vide
        self.boites = {}

        for idx_boite_horizontale in range(self.N_BOITES_H):  # Crée les boites
            for idx_boite_verticale in range(self.N_BOITES_V):
                self.boites[(idx_boite_horizontale, idx_boite_verticale)] = Boite()

    def coup_dans_les_limites(self, index_ligne):
        """
        ÉTAPE 2

        Vérifie si un coup est dans les limites de la planche.
        Dans notre cas, comme tous les index valides de lignes
        dans la planche sont des clés dans le dictionnaire
        self.lignes, il nous suffit de vérifier que l'index
        en entrée est contenu dans les clés de self.lignes.

        Args :
            index_ligne (int, int, str): index de la ligne

        Returns :
            bool: True si le coup est dans les limites, False sinon

        TODO: Vous devez compléter le corps de cette fonction.
        """

        return index_ligne in self.lignes

    def est_pleine(self):
        """
        ÉTAPE 2

        Méthode qui vérifie si la planche est pleine.

        Une planche est pleine si toutes ses lignes sont
        jouées.

        N.B. Chaque ligne possède un attribut booléen
            ligne.jouee qui est à True si la ligne est jouée.

        Returns :
            bool : True si la grille est pleine, False sinon

        TODO: Vous devez compléter le corps de cette fonction.
        """

        for ligne in self.lignes.values():
            if not ligne.jouee:
                return False
        return True

    def jouer_coup(self, index_ligne, couleur):
        """
        ÉTAPE 2

        Méthode qui va gérer la logique de jeu d'un coup dans
        la planche de pipopipette.

        Cette méthode doit donc:
        - Mettre à jour les attributs couleur_dernier_coup et
          position_dernier_coup en leur assignant les arguments
          en entrée couleur et index_ligne, respectivement
        - Mettre à jour l'attribut jouee de la ligne située à
          l'index joué

        Args :
            index_ligne (int, int, str): L'index de la ligne jouée
            couleur (str): La couleur du joueur qui joue la ligne

        TODO: Vous devez compléter le corps de cette fonction.
        """

        self.position_dernier_coup = index_ligne
        self.couleur_dernier_coup = couleur
        self.lignes[index_ligne].jouee = True

    def valider_coup(self, index_ligne):
        """
        ÉTAPE 2

        Méthode permettant de vérifier la validité d'un coup.

        Dans le contexte du jeu de pipopipette, un coup est un
        index de ligne au format (int, int, str).

        Un coup est invalide (1) si son orientation n'est pas
        'H' ni 'V', (2) s'il n'est pas dans les limites
        ou (3) s'il est tenté sur une ligne déjà jouée. On
        retourne False ainsi qu'un message d'erreur approprié
        selon la raison de l'échec pour un coup invalide.

        Pour le cas (2), la classe Planche possède la méthode
        coup_dans_les_limites(), utilisez la !

        N.B. : Pour retourner deux valeurs comme vous le demande
            cette fonction, vous n'avez qu'à les séparer d'une virgule:

            return valeur_1, valeur_2

        Args :
            index_ligne (int, int, str): l'index de la ligne jouée

        Returns :
            bool: True si le coup est valide, False sinon

            str: message d'erreur approprié si le coup est invalide, None sinon

        TODO: Vous devez compléter le corps de cette fonction.
        """

        definition_erreur_2 = 'est en dehors des limites de la grille.\n'
        definition_erreur_3 = 'est une ligne déjà jouée. Recommencez\n'

        # try:
        #     if not self.coup_dans_les_limites(index_ligne):  # cond.2: vérifie si le coups est dans les limites
        #         raise ErreurPositionCoup(index_ligne)
        # except ErreurPositionCoup as e:
        #     print(e, definition_erreur_2)
        #     messagebox.showinfo("Window", definition_erreur_2)

        try:
            if self.lignes[index_ligne].jouee:  # cond.3: vérifie si la ligne est déjà jouée
                raise ErreurPositionCoup(index_ligne)
        except ErreurPositionCoup as e:
            print(e, definition_erreur_3)
            messagebox.showinfo("Window", definition_erreur_3)
            return False

        return True

    def obtenir_coups_possibles(self):
        """
        ÉTAPE 2

        Obtient la liste de tous les coups possibles.

        Returns :
            List[(int, int, str)]: liste des index de toutes les lignes non jouées de la planche

        TODO: Vous devez compléter le corps de cette fonction.
        """
        return [idx for idx, ligne in self.lignes.items() if not ligne.jouee]

    def maj_boites(self):
        """
        ÉTAPE 3

        Cette méthode effectue la mise à jour des boîtes après un coup.

        Elle commence par obtenir les index des boîtes à valider (seulement
        les boîtes qui touchent à la ligne jouée) avec la méthode
        self.obtenir_idx_boites_a_valider() et ensuite leur assigner la bonne couleur
        au besoin avec la méthode self.valider_boites().

        Returns:
            bool: Le retour de self.valider_boites(). (True si une boîte a
                été remplie par le dernier coup, False sinon.)

        TODO: Vous devez compléter le corps de cette fonction.
        """

        # obtient l'index des boites à valider
        boites_a_valider = self.obtenir_idx_boites_a_valider()

        return self.valider_boites(boites_a_valider)

    def obtenir_idx_boites_a_valider(self):
        """
        ÉTAPE 3

        Méthode qui retourne les index de toutes les boîtes qui touchent à
        la dernière ligne jouée. Vous pouvez accéder à l'index de la dernière
        ligne jouée avec l'attribut self.position_dernier_coup.

        La ou les boîtes à valider dépendent de l'orientation du dernier coup :

        - Si la dernière ligne était verticale (orientation == 'V'), les boîtes
          lui touchant sont celles correspondant à (ligne, colonne) et
          (ligne, colonne - 1), soit les boîtes à la gauche et la droite de la ligne.

        - Si la dernière ligne était horizontale (orientation == 'H'), les boîtes
          lui touchant sont celles correspondant à (ligne, colonne) et
          (ligne - 1, colonne), soit les boîtes supérieure et inférieure à la ligne.

        Notez qu'il est possible que l'une des deux boîtes énoncées plus haut
        soit hors limites. Par exemple, si la dernière ligne jouée était la
        ligne horizontale du haut gauche (0, 0, 'H'), on aura une boîte inférieure
        à l'index (0, 0) mais aucune boîte supérieure à l'index (0, -1) car l'index
        est en dehors des limites de la planche.

        Votre fonction doit donc s'assurer que chacun des index retournés correspond
        à l'index d'une boîte valide. Pour faire la validation qu'un index de boîte
        est valide, vous pouvez simplement vérifier si ledit index est présent dans les
        clés de self.boites.

        Returns:
            List[(int, int)]: la liste des index des boîtes touchés par le dernier coup

        TODO: Vous devez compléter le corps de cette fonction.
        """

        ligne, colonne, orientation = self.position_dernier_coup

        boite_1 = ''
        boite_2 = ''
        boites_touchees = []

        # calcul les index des boites touchées par le coup
        if orientation == 'V':
            boite_1 = (ligne, colonne)
            boite_2 = (ligne, colonne - 1)

        if orientation == 'H':
            boite_1 = (ligne, colonne)
            boite_2 = (ligne - 1, colonne)

        # vérifie si l'index de la boite touchée est dans les limites
        if boite_1 in self.boites:
            boites_touchees.append(boite_1)

        if boite_2 in self.boites:
            boites_touchees.append(boite_2)

        return boites_touchees

    def compter_lignes_jouees_boite(self, idx_boite):
        """
        ÉTAPE 3

        Méthode qui compte le nombre de lignes qui sont jouées autour de l'index
        d'une boîte.

        On vérifie donc les lignes (1) verticale gauche, (2) verticale
        droite, (3) horizontale supérieure et (4) horizontale inférieure de la boîte.
        Vous devez utiliser l'index de la boîte pour retrouver l'index de chacune
        des quatre lignes à valider.

        Pour savoir si une ligne est jouée, il suffit de vérifier si son attribut
        ligne.jouee est True.

        Args:
            idx_boite (int, int): L'index la boîte autour de laquelle on valide.

        Returns:
            int: le nombre de lignes jouées autour de la boîte.

        TODO: Vous devez compléter le corps de cette fonction.
        """

        idx_ligne, idx_colonne = idx_boite

        ligne_verti_gauche = (idx_ligne, idx_colonne, 'V')
        ligne_verti_droite = (idx_ligne, idx_colonne + 1, 'V')
        ligne_horiz_super = (idx_ligne, idx_colonne, 'H')
        ligne_horiz_infer = (idx_ligne + 1, idx_colonne, 'H')

        lignes_de_la_boite = [ligne_verti_gauche, ligne_verti_droite, ligne_horiz_super, ligne_horiz_infer]
        nb_ligne_jouee = 0

        for ligne in lignes_de_la_boite:
            ligne = self.lignes[ligne]
            if not ligne.jouee:
                nb_ligne_jouee += 0
                continue

            if ligne.jouee:
                nb_ligne_jouee += 1  # calcul le nombre de lignes jouées autour
                # d'une boite

        return nb_ligne_jouee

    def valider_boites(self, idx_boites):
        """
        ÉTAPE 3

        Méthode qui fait la validation de l'état des boîtes dans une liste
        d'index.

        La validation d'une boîte se fait comme suit:

        - Si la boîte est déjà pleine (son attribut pleine est True),
          on ne fait rien et on passe à la prochaine boîte.

        - Sinon, on compte les nombre de lignes jouées autour de la boîte
          avec la méthode self.compter_lignes_jouees_boites(). Si le nombre
          de lignes autour de la boite est 4, c'est que la boîte est maintenant
          pleine. Si la boîte est maintenant pleine, on fait appel à la méthode
          assigner_couleur() de Boite en passant comme argument la couleur du
          dernier coup contenue dans self.couleur_dernier_coup.

        Enfin, on retourne une valeur booléene correpondant à si au moins une
        des boîtes est maintenant remplie.

        Args:
            idx_boites (List[(int, int)]): la liste des index des boîtes à valider

        Returns:
            bool: True si au moins une des boîtes est maintenant remplie, False
                sinon.

        TODO: Vous devez compléter le corps de cette fonction.
        """

        au_moins_une_boite_remplie = False

        for idx_boite in idx_boites:

            boite = self.boites[idx_boite]
            if not boite.pleine:
                nb_lignes_jouees_boite = self.compter_lignes_jouees_boite(idx_boite)

                if nb_lignes_jouees_boite == 4:
                    boite.assigner_couleur(self.couleur_dernier_coup)
                    au_moins_une_boite_remplie = True

        return au_moins_une_boite_remplie

    def bilan_boites(self):
        """
        ÉTAPE 3

        Méthode qui calcule le nombre de boîtes associées à chacun des joueurs en
        fonction de leur couleur.

        On itère donc sur toutes les boîtes de l'attribut self.boites et, pour savoir
        si une boîte est de la couleur rouge, on teste seulement si son attribut
        boite.couleur est égal à 'rouge'. Idem pour la couleur bleue.

        On retourne ensuite, dans l'ordre, le nombre de boîte bleues et de boîtes rouges.

        N.B. Pour retourner plus d'une valeur dans une fonction, il suffit de les
             séparer par une virgule i.e.

             return valeur_1, valeur_2

        Returns:
            int: Le nombre de boîtes bleues dans la planche
            int: le nombre de boîtes rouges dans la planche

        TODO: Vous devez compléter le corps de cette fonction.
        """

        n_boites_bleues = sum([boite.couleur == 'bleu' for boite in self.boites.values()])
        n_boites_rouges = sum([boite.couleur == 'rouge' for boite in self.boites.values()])

        return n_boites_bleues, n_boites_rouges

    def __repr__(self):
        """
        Cette méthode spéciale permet de modifier le comportement
        d'une instance de la classe Planche pour l'affichage.

        Faire un print(une_planche) affichera la planche à l'écran.
        """
        decalage_nouvelle_ligne = '\n' + ' ' * 3
        planche = ''

        planche += decalage_nouvelle_ligne

        for idx_colonne in range(Planche.N_BOITES_V + 1):
            planche += '{:<4}'.format(idx_colonne)

        for idx_ligne in range(Planche.N_BOITES_H):
            planche += decalage_nouvelle_ligne

            # On commence par dessiner la ligne du haut de la planche
            for idx_colonne in range(Planche.N_BOITES_V):
                planche += '+'
                planche += '---' if self.lignes[(idx_ligne, idx_colonne, 'H')].jouee else '   '

            planche += '+{:>2}'.format(idx_ligne) + decalage_nouvelle_ligne

            # On rajoute les lignes verticales et la couleur des boîtes
            for idx_colonne in range(Planche.N_BOITES_V):
                planche += '|' if self.lignes[(idx_ligne, idx_colonne, 'V')].jouee else ' '
                planche += '{:^3}'.format(self.boites[(idx_ligne, idx_colonne)].couleur_formattee())

            # On rajoute la ligne verticale du bout
            planche += '|' if self.lignes[(idx_ligne, Planche.N_BOITES_V, 'V')].jouee else ' '

        planche += decalage_nouvelle_ligne

        # On rajoute la ligne horizontale du bas
        for idx_colonne in range(Planche.N_BOITES_V):
            planche += '+'
            planche += '---' if self.lignes[(Planche.N_BOITES_H, idx_colonne, 'H')].jouee else '   '

        planche += '+{:>2}'.format(Planche.N_BOITES_H) + decalage_nouvelle_ligne

        return planche

