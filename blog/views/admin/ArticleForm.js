import React, { Component } from 'react';
//import style from './style';

export default class ArticleForm extends Component {
  constructor(props) {
    super(props);
    this.state = { 
      title: '',
      published: false, 
      category: '',
      body: '',
      author: '',
      postedOn: '',
      updatedOn: ''
    };

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(e) {
    e.preventDefault();
    let title = this.state.title.trim();
    let published = this.state.published;
    let category = this.state.category.trim();
    let body = this.state.body.trim();
    let author = this.state.author.trim();
    let postedOn = this.state.postedOn;
    let updatedOn = this.state.updatedOn;
    
    if(!title || !body) {
      return;
    }
  
    this.props.onArticleSubmit( {
      title: title,
      published: published,
      category: category,
      body: body,
      author: author,
      postedOn: postedOn,
      updatedOn: updatedOn
    });

    this.setState({
      title: '',
      published: false,
      category: '',
      body: '',
      author: '',
      postedOn: '',
      updatedOn: ''
    });
  }

  render() {
    return (
       <div>
            <h1>Add new Article</h1>
            <form onSubmit={ this.handleSubmit }>
                <div className="form-group">
                    <label for="title">Title</label>
                    <input type="text" className="form-control"
                     id="title"
                     aria-describedby="Title"
                     placeholder="Title"/>
                </div>

                <div className="form-group">
                    <label for="published">Title</label>
                    <input type="checkbox" className="form-control"
                     id="published"
                     aria-describedby="Published"
                     placeholder="Title"/>
                </div>

                <div className="form-group">
                    <label for="category">Priority</label>
                    <select className="form-control" 
                    id="category">
                        <option>PHP</option>
                        <option>NodeJS</option>
                        <option>Business Management</option>
                    </select>
                </div>

                <div className="form-group">
                    <label for="body">Body</label>
                    <input type="text" className="form-control" 
                     id="body" placeholder="Body Text..."/>
                </div>

                <button type="submit" className="btn btn-primary">Add</button>
                <button type="cancel" className="btn btn-danger">Cancel</button>
            </form>
           </div>
    );
  }
}
