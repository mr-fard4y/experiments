
console.log(React);
console.log(ReactDOM);

var App = React.createClass({
    render: function() {
        return (
            <div className="app">
                Hi, Here is a first react component!
            </div>
        );
    }
});

ReactDOM.render(
    <App />,
    document.getElementById('root')
);
