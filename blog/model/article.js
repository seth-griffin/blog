'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ArticleSchema = new Schema({
  title: String,
  published: Boolean,
  category: String,
  body: String,
  author: String,
  postedOn: Date,
  updatedOn: Date
});

module.exports = mongoose.model('Article', ArticleSchema);
