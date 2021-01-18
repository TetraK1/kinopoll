'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

class PollVote extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      title: 'Poll',
      questions: [
        'yuh',
      ],
    }
  }
  render() {
    return e('div', {}, 'yuh')
  }
}

const domContainer = document.querySelector('#react');
ReactDOM.render(e(LikeButton), domContainer);
ReactDOM.render(e(PollVote), domContainer);