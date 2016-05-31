import React from 'react';
import AutoComplete from 'material-ui/AutoComplete';

class SearchBar extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      dataSource: ['Toulouse', 'Paris'],
    };
  }

  handleUpdateInput(value) {
    this.setState({
      dataSource: [
        value,
        value + value,
        value + value + value,
      ],
    });
  }

  render() {
    return (
      <div>
        <AutoComplete
          hintText="Type anything"
          dataSource={this.state.dataSource}
          onUpdateInput={this.handleUpdateInput}
        />
      </div>
    );
  }
}

export default SearchBar;
