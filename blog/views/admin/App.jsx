import React, { Component } from 'react';
//import style from './style';
import ArticleForm from './ArticleForm';
import ArticleList from './ArticleList';

import axios from 'axios';

class App extends Component {

    constructor(props) {
        super(props);
        this.apiUrl = '/api/v1';

        this.state = { 
            articles: [], 
            categories: [] 
        };

        this.loadArticlesFromServer = this.loadArticlesFromServer.bind(this);
        this.loadCategoriesFromServer = this.loadCategoriesFromServer.bind(this);
        this.handleArticleSubmit = this.handleArticleSubmit.bind(this);
        this.handleArticleDelete = this.handleArticleDelete.bind(this);
        this.handleArticleUpdate = this.handleArticleUpdate.bind(this);
    }

    loadArticlesFromServer() {
        axios.get(`${this.apiUrl}/article/all`)
            .then(res => {
                this.setState({ articles: res.data })
            })
    }

    loadCategoriesFromServer() {
        axios.get(`${this.apiUrl}/category/all`)
            .then(res => {
                this.setState({ categories: res.data })
            })
    }

    handleArticleSubmit(article) {
        let articles = this.state.articles;
        let newArticles = articles.concat([article]);
        this.setState( { articles: newArticles });
        axios.post(`${this.apiUrl}/article`, article)
            .catch(err => {
                console.error(err);
            });
    }

    handleArticleDelete(id) {
        axios.delete(`${this.apiUrl}/article/${id}`)
            .then(res => {
                console.log('Article deleted');
            })
            .catch(err => {
                console.error(err);
            });
    }

    handleArticleUpdate(id, article) {
        //sends the comment id and new author/text to our api
        axios.put(`${this.apiUrl}/${id}`, article)
            .catch(err => {
                console.log(err);
            })
    }

    componentDidMount() {
        this.loadArticlesFromServer();
        this.loadCategoriesFromServer();
        setInterval(this.loadArticlesFromServer, this.props.pollInterval);
        setInterval(this.loadCategoriesFromServer, this.props.pollInterval);
    }


   render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src="./images/logo.svg" 

          className="App-logo" alt="logo" />
          <h2>Blog Admin</h2>
        </div>
          <ArticleList

              onArticleDelete={ this.handleArticlDelete }

              onArticleUpdate={ this.handleArticleUpdate }

              data={ this.state.articles } />

          <ArticleForm onArticleSubmit={ this.handleArticleSubmit } categories={ this.state.categories } />


      </div>
    );
  }
}

export default App;
