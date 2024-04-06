
console.log(React);
console.log(ReactDOM);

var App = React.createClass({
    render: function() {
        return (
            <div className="app">
                First app
                <News />
                <Comments />
            </div>
        );
    }
});

var News = React.createClass({
    render: function() {
        return (
            <div className="news">
                News: Nothing to show.
            </div>
        )
    }
})

var Comments = React.createClass({
    render: function() {
        return (
            <div className="comments">
                Comments: Nothing to show.
            </div>
        )
    }
})

ReactDOM.render(
    <App />,
    document.getElementById('root')
);
