import React, { Component } from 'react';
//import style from './style';
import ArticleForm from './ArticleForm';
import ArticleList from './ArticleList';

import axios from 'axios';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = { data: [] };
        this.apiUrl = '/api/v1';
        this.loadArticlesFromServer = this.loadArticleFromServer.bind(this);
        this.handleArticleSubmit = this.handleArticleSubmit.bind(this);
        this.handleArticleDelete = this.handleArticleDelete.bind(this);
        this.handleArticleUpdate = this.handleArticleUpdate.bind(this);
    }

    loadArticleFromServer() {
        axios.get(this.props.url)
            .then(res => {
                this.setState({ data: res.data });
            })
    }

    handleArticleSubmit(article) {
        let articles = this.state.data;
        let newArticles = articles.concat([article]);
        this.setState({ data: newArticles });
        axios.post(`${this.apiUrl}/article`, article)
            .catch(err => {
                console.error(err);
                this.setState({ data: article });
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
        setInterval(this.loadArticlesFromServer, this.props.pollInterval);
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

              data={ this.state.data }/>

          <ArticleForm onArticleSubmit={ this.handleArticleSubmit }/>


      </div>
    );
  }
}

export default App;
