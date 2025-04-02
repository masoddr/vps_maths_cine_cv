describe('Dashboard Page', () => {
  beforeEach(() => {
    // Simuler la connexion de l'utilisateur
    cy.intercept('POST', '**/api/login', {
      statusCode: 200,
      body: {
        id: 1,
        email: 'test@example.com',
        name: 'Test User'
      }
    }).as('loginRequest')

    // Simuler les données de progression
    cy.intercept('GET', '**/api/progress/stats', {
      statusCode: 200,
      body: {
        global: 65,
        completedExercises: 13,
        totalExercises: 20,
        totalHours: 24,
        masteredTopics: 3,
        totalTopics: 5
      }
    }).as('statsRequest')

    // Simuler la liste des exercices
    cy.intercept('GET', '**/api/progress', {
      statusCode: 200,
      body: [
        {
          id: 1,
          title: 'Dérivées et Primitives',
          examPaper: 'Bac 2023 - Série S',
          status: 'completed'
        },
        {
          id: 2,
          title: 'Suites Numériques',
          examPaper: 'Bac 2023 - Série S',
          status: 'in_progress'
        }
      ]
    }).as('exercisesRequest')

    // Visiter la page du tableau de bord
    cy.visit('/dashboard')
  })

  it('affiche correctement les statistiques de progression', () => {
    cy.wait(['@statsRequest', '@exercisesRequest'])

    // Vérifier les cartes de statistiques
    cy.contains('65%')
    cy.contains('13 exercices terminés sur 20')
    cy.contains('24h')
    cy.contains('3/5')
  })

  it('affiche la liste des exercices', () => {
    cy.wait(['@statsRequest', '@exercisesRequest'])

    // Vérifier les exercices affichés
    cy.contains('Dérivées et Primitives')
    cy.contains('Suites Numériques')
    cy.contains('Bac 2023 - Série S')
  })

  it('permet de mettre à jour le statut d\'un exercice', () => {
    cy.wait(['@statsRequest', '@exercisesRequest'])

    // Simuler la réponse de l'API pour la mise à jour du statut
    cy.intercept('POST', '**/api/progress/2', {
      statusCode: 200,
      body: {
        id: 2,
        status: 'completed'
      }
    }).as('updateRequest')

    // Simuler la nouvelle réponse des stats après la mise à jour
    cy.intercept('GET', '**/api/progress/stats', {
      statusCode: 200,
      body: {
        global: 70,
        completedExercises: 14,
        totalExercises: 20,
        totalHours: 24,
        masteredTopics: 3,
        totalTopics: 5
      }
    }).as('updatedStatsRequest')

    // Cliquer sur le bouton pour marquer l'exercice comme terminé
    cy.contains('Suites Numériques')
      .parent()
      .parent()
      .parent()
      .find('button')
      .contains('Marquer comme terminé')
      .click()

    // Vérifier que la requête a été envoyée
    cy.wait('@updateRequest')
    cy.wait('@updatedStatsRequest')

    // Vérifier que les statistiques ont été mises à jour
    cy.contains('70%')
    cy.contains('14 exercices terminés sur 20')
  })

  it('gère les erreurs de chargement', () => {
    // Simuler une erreur lors du chargement des stats
    cy.intercept('GET', '**/api/progress/stats', {
      statusCode: 500,
      body: {
        error: 'Erreur serveur'
      }
    }).as('failedStatsRequest')

    cy.visit('/dashboard')
    cy.wait('@failedStatsRequest')

    // Vérifier que les valeurs par défaut sont affichées
    cy.contains('0%')
    cy.contains('0 exercices terminés sur 0')
  })
}) 