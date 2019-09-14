import React, { Component } from 'react';


export default class ArticleList extends Component {
    render() {
        let articleNodes = this.props.data.map(article => {
            return (
              <tr>
                <td> 
                  { article.title }
                </td>
                <td>
                  { article.category }
                </td>
                <td>
                  { article.published ? "Yes" : "No" }
                </td>
                <td>
                  <button type="submit" className="btn btn-primary">
                    Edit
                  </button>
                  <button type="submit" className="btn btn-primary">
                    { article.published ? "Unpublish" : "Publish"}
                  </button>
                </td>
              </tr>
            )
        })

        return (
            <div className="panel panel-success">
                <h1> Articles </h1>
                <table>
                  <thead>
                    <tr>
                      <th>Title</th><th>Category</th><th>Published</th><th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    { articleNodes }
                  </tbody>
                </table>                
            </div>
        )
    }
}
