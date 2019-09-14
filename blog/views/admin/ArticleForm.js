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

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const target = event.target;

    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.state[name] = value;
    this.setState(this.state); 
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
    var categories = this.props.categories.map((category) => <option>{category.name}</option>);
    return (
       <div>
            <h1>Add new Article</h1>
            <form onSubmit={ this.handleSubmit }>
                <div className="form-group">
                    <label for="title">Title</label>
                    <input type="text" className="form-control"
                      id="title"
                      name="title"                     
                      aria-describedby="Title"
                      placeholder="Title"
                      onChange={ this.handleChange } />
                </div>

                <div className="form-group">
                    <label for="published">Publish</label>
                    <input type="checkbox" 
                      className="form-control"
                      id="published"
                      name="published"
                      aria-describedby="Published"
                      placeholder="Published"
                      onChange= { this.handleChange } />
                </div>

                <div className="form-group">
                    <label for="category">Category</label>
                    <select 
                      className="form-control" 
                      id="category"
                      name="category"
                      onChange={ this.handleChange }>
                        { categories }
                   </select>                  
                </div>

                <div className="form-group">
                    <label for="body">Article</label>
                    <textarea type="text" 
                      className="form-control" 
                      id="body" 
                      name="body" 
                      placeholder="Body Text..."
                      onChange={ this.handleChange }>
                      </textarea>
                </div>

                <button type="submit" className="btn btn-primary">Add</button>
                <button type="cancel" className="btn btn-danger">Cancel</button>
            </form>
           </div>
    );
  }
}
