Voici une description concise de l'utilisation de chaque fichier HTML dans votre application gestion_projets :

base.html :
Sert de modèle de base pour la mise en page de l’application.
Contient le menu de navigation commun et structure les sections que les autres templates peuvent étendre.

projet_list.html :
Affiche la liste de tous les projets enregistrés.
Fournit des liens vers les détails de chaque projet.

projet_detail.html :
ffiche les détails d’un projet spécifique, comme son nom, sa description, et son statut.
Montre également la liste des tâches associées au projet et offre des options pour ajouter une nouvelle tâche ou modifier le projet.

projet_create.html :
Affiche un formulaire pour créer un nouveau projet.
Enregistre le projet dans la base de données lorsqu’il est soumis.

projet_edit.html :
Affiche un formulaire pour modifier un projet existant.
Enregistre les modifications apportées au projet lorsqu’il est soumis.

tache_create.html :
Affiche un formulaire pour ajouter une nouvelle tâche à un projet spécifique.
Associe automatiquement la tâche au projet en cours et l’enregistre.

task_form.html (optionnel) :
Sert de template générique pour les formulaires de tâches, que ce soit pour la création ou l’édition.
Peut être utilisé pour rendre les formulaires de tâche plus modulaires et réutilisables dans différents contextes.
