describe('Tests Responsive', () => {
  const viewports = {
    mobile: [375, 667],    // iPhone SE
    tablet: [768, 1024],   // iPad
    desktop: [1280, 800],  // Desktop standard
  }

  describe('Page d\'accueil', () => {
    beforeEach(() => {
      cy.visit('/')
    })

    Object.entries(viewports).forEach(([device, [width, height]]) => {
      it(`s'affiche correctement sur ${device}`, () => {
        cy.viewport(width, height)
        
        // Vérifier le header
        if (device === 'mobile') {
          // Sur mobile, le menu doit être caché dans un menu burger
          cy.get('nav').find('button').should('be.visible')
          cy.get('nav').find('.sm\\:flex').should('not.be.visible')
        } else {
          // Sur tablet et desktop, le menu doit être visible
          cy.get('nav').find('.sm\\:flex').should('be.visible')
        }

        // Vérifier la section hero
        cy.get('h1').should('be.visible')
        cy.contains('Réussis ton Bac').should('be.visible')
        
        // Vérifier les boutons d'action
        cy.contains('Commencer gratuitement').should('be.visible')
        cy.contains('Voir les annales').should('be.visible')
      })
    })
  })

  describe('Page Tableau de bord', () => {
    beforeEach(() => {
      // Simuler la connexion
      cy.intercept('POST', '**/api/login', {
        statusCode: 200,
        body: { id: 1, email: 'test@example.com' }
      })

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
      })

      cy.intercept('GET', '**/api/progress', {
        statusCode: 200,
        body: []
      })

      cy.visit('/dashboard')
    })

    Object.entries(viewports).forEach(([device, [width, height]]) => {
      it(`affiche correctement les cartes de statistiques sur ${device}`, () => {
        cy.viewport(width, height)
        
        // Vérifier l'organisation des cartes
        if (device === 'mobile') {
          // Sur mobile, les cartes doivent être empilées
          cy.get('.grid').should('have.class', 'grid-cols-1')
        } else if (device === 'tablet') {
          // Sur tablet, 2 colonnes
          cy.get('.grid').should('have.class', 'sm:grid-cols-2')
        } else {
          // Sur desktop, 3 colonnes
          cy.get('.grid').should('have.class', 'lg:grid-cols-3')
        }

        // Vérifier que toutes les cartes sont visibles
        cy.contains('Progression globale').should('be.visible')
        cy.contains('Temps de révision').should('be.visible')
        cy.contains('Thèmes maîtrisés').should('be.visible')
      })
    })
  })

  describe('Page Annales', () => {
    beforeEach(() => {
      // Simuler les données des annales
      cy.intercept('GET', '**/api/exampapers', {
        statusCode: 200,
        body: [
          {
            id: 1,
            title: 'Bac 2024 - Métropole',
            year: 2024,
            pdfUrl: '/test.pdf'
          }
        ]
      })

      cy.visit('/annales')
    })

    Object.entries(viewports).forEach(([device, [width, height]]) => {
      it(`adapte correctement les filtres et la liste sur ${device}`, () => {
        cy.viewport(width, height)
        
        // Vérifier les filtres
        if (device === 'mobile') {
          // Sur mobile, les filtres doivent être empilés
          cy.get('.grid').first().should('have.class', 'grid-cols-1')
        } else {
          // Sur tablet et desktop, les filtres doivent être en ligne
          cy.get('.grid').first().should('have.class', 'sm:grid-cols-4')
        }

        // Vérifier que la barre de recherche est toujours visible
        cy.get('input[type="text"]').should('be.visible')
        
        // Vérifier que les filtres sont accessibles
        cy.get('select#year').should('exist')
        cy.get('select#theme').should('exist')
      })

      it(`gère correctement le zoom PDF sur ${device}`, () => {
        cy.viewport(width, height)
        
        // Cliquer sur une annale pour ouvrir le PDF
        cy.contains('Bac 2024 - Métropole').click()
        
        // Vérifier que le PDF s'ouvre dans une nouvelle fenêtre ou un modal adapté
        if (device === 'mobile') {
          // Sur mobile, vérifier que le PDF s'ouvre en plein écran
          cy.get('.modal').should('have.class', 'fullscreen')
        } else {
          // Sur desktop, vérifier que le PDF s'ouvre dans un modal avec des contrôles de zoom
          cy.get('.modal').should('have.class', 'with-zoom-controls')
          cy.get('.zoom-controls').should('be.visible')
        }
      })
    })
  })
}) 