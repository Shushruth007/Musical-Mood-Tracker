import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import './App.css';



var dict = {
  Great: rgb(1, 151, 18),
  Good: rgb(174, 255, 0),
  Okay: rgb(251, 255, 0),
  Sad: rgb(255, 170, 0),
  VerySad: rgb(255, 0, 0)
};



class App extends React.Component {
  constructor(props)
  {
    super(props)
    this.state={
      date:new Date(),
      dayColor: "red"
    }
  }

  previouslySelectedDates = []

   tileClass = ({date, view}) => {
    if (view == 'month') {
      if (previouslySelectedDates.find(currentDate => currentDate == date)) {
        return 'newClass'
      }
    }
   }

  onChange = date => {
    this.previouslySelectedDates.add(date)
    this.setState({ date })
  }
  render()
  {

  return (

    <div className="App">

       <Calendar
          onChange={this.onChange}
          value={this.state.date}
          tileClassName={tileClass}

        />
    </div>


  );
  }
}

export default App;
