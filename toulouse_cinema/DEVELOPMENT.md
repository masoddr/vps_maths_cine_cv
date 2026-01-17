# Guide de développement local

Ce guide explique comment lancer un environnement de développement local avec rechargement automatique, sans impacter la production.

## 🚀 Démarrage rapide

Pour lancer l'environnement de développement :

```bash
./dev-start.sh
```

Ou manuellement :

```bash
docker-compose -f docker-compose.dev.yml up --build
```

L'application sera accessible sur **http://localhost:3001**

## 📋 Fonctionnalités

- ✅ **Hot-reload automatique** : Les modifications dans le code sont automatiquement reflétées dans le navigateur
- ✅ **Production intacte** : L'environnement de production continue de fonctionner normalement
- ✅ **Port différent** : Le développement utilise le port 3000, la production le port 3001
- ✅ **Volumes montés** : Le code source est monté dans le conteneur pour un rechargement instantané

## 🛠️ Commandes utiles

### Démarrer en arrière-plan
```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Voir les logs
```bash
docker-compose -f docker-compose.dev.yml logs -f
```

### Arrêter l'environnement de développement
```bash
docker-compose -f docker-compose.dev.yml down
```

### Reconstruire les images
```bash
docker-compose -f docker-compose.dev.yml up --build
```

## 🔄 Différences avec la production

| Aspect | Développement | Production |
|--------|--------------|------------|
| Port | 3001 | 3001 |
| Mode | `npm run dev` | `npm run build` + serveur Node |
| Hot-reload | ✅ Activé | ❌ Désactivé |
| Prerender | ❌ Désactivé | ✅ Activé |
| Traefik | ❌ Non utilisé | ✅ Configuré |
| Volumes | Code source monté | Build statique |

## 📝 Notes importantes

- L'environnement de développement utilise un réseau Docker séparé (`dev_network`)
- Les modifications dans `frontend/` sont immédiatement visibles grâce aux volumes montés
- Le prerender est désactivé en développement pour améliorer les performances du hot-reload
- La production reste accessible sur `cinephoria.fr` pendant que vous développez

## 🐛 Dépannage

### Le port 3001 est déjà utilisé
Modifiez le port dans `docker-compose.dev.yml` :
```yaml
ports:
  - "3002:3000"  # Changez 3001 à gauche par un autre port (ex: 3002)
```

### Les modifications ne se reflètent pas
1. Vérifiez que les volumes sont bien montés : `docker-compose -f docker-compose.dev.yml config`
2. Redémarrez le conteneur : `docker-compose -f docker-compose.dev.yml restart`

### Erreurs de dépendances
Réinstallez les dépendances dans le conteneur :
```bash
docker-compose -f docker-compose.dev.yml exec frontend_dev npm install
```
