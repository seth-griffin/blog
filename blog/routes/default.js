var express = require('express');
var mongojs = require('mongojs');
var router = express.Router();
var db = mongojs('mongodb://localhost:27017/blog', ['article', 'category']);
/*** Pages ***/ 

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('page', { title: 'Seth Griffin\'s blog' });
});

/*** API ***/

/** V1 **/

/* Article */

/* GET all articles */
router.get('/api/v1/article/all', function(req, res, next) {
  db.article.find(function(err, article) {
    if(err) {    
      res.send(err);
    }
    res.json(article);
  });

});

/* GET single article by id */
 
router.get('/api/v1/article/:id', function(req, res, next) {
  db.article.findOne({_id: mongojs.ObjectId(req.params.id)}, function(err, article) {
    if(err) {
      res.send(err);
    }
    res.json(article);
  });

});

/* POST new article */

router.post('/api/v1/article', function(req, res, next) {
  var article = req.body;

  db.article.save(article, function(err, article) {
    if(err) {
      res.send(err);
    }
    res.json(article);
  });

});

/* PUT existing article */

router.put('/api/v1/article/:id', function(req, res, next) {
  var article = req.body;

  db.article.update({_id: mongojs.ObjectId(req.params.id)}, article, function(err, article) {
    if(err) {
      res.send(err);
    }
    res.json(article);
  }); 

}); 

/* DELETE existing article by id */

router.delete('/api/v1/article/:id', function(req, res, next) {
  db.article.remove({_id: mongojs.ObjectId(req.params.id)}, function(err, article) {
    if(err) {
      res.send(err);
    }
    res.json(article);
  }); 
});

/* Category */

/* GET all categories */
router.get('/api/v1/category/all', function(req, res, next) {
  db.category.find(function(err, category) {
    if(err) {
      res.send(err);
    }
    res.json(category);
  });

});

/* GET single category by id */

router.get('/api/v1/category/:id', function(req, res, next) {
  db.category.findOne({_id: mongojs.ObjectId(req.params.id)}, function(err, category) {
    if(err) {
      res.send(err);
    }
    res.json(category);
  });

});

/* POST new category */

router.post('/api/v1/category', function(req, res, next) {
  var category = req.body;

  db.category.save(category, function(err, category) {
    if(err) {
      res.send(err);
    }
    res.json(category);
  });

});

/* PUT existing category */

router.put('/api/v1/category/:id', function(req, res, next) {
  var category = req.body;

  db.category.update({_id: mongojs.ObjectId(req.params.id)}, category, function(err, category) {
    if(err) {
      res.send(err);
    }
    res.json(category);
  });

});

/* DELETE existing category by id */

router.delete('/api/v1/category/:id', function(req, res, next) {
  db.category.remove({_id: mongojs.ObjectId(req.params.id)}, function(err, category) {
    if(err) {
      res.send(err);
    }
    res.json(category);
  });
});


module.exports = router;
