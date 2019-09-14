import React, { Component } from 'react';


export default class CategoryList extends Component {
    render() {
        let catgoryNodes = this.props.data.map(category => {
            return (
              <tr>
                <td> 
                  { category.title }
                </td>
                <td>
                  { category.description }
                </td>
                <td>
                  <button type="submit" className="btn btn-primary">
                    Edit
                  </button>
                </td>
              </tr>
            )
        })

        return (
            <div className="panel panel-success">
                <h1> Categories </h1>
                <table>
                  <thead>
                    <tr>
                      <th>Title</th><th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    { categoryNodes }
                  </tbody>
                </table>
            </div>
        )
    }
}
