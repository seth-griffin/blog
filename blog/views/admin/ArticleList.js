import React, { Component } from 'react';


export default class ArticleList extends Component {
    render() {
        let articleNodes = this.props.data.map(article => {
            return (
                <div className="panel panel-primary">
                    Title : {article.title}
                </div>
            )
        })

        return (

            <div className="panel panel-success">
                <h1> All Articles </h1>
                { articleNodes }
            </div>
        )
    }
}
