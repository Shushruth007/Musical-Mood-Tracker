import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import './App.css';


import { isWithinInterval } from "date-fns";
import { differenceInCalendarDays } from 'date-fns';

function isSameDay(a, b) {
  return differenceInCalendarDays(a, b) === 0;
}

function isWithinRange(date, range) {
  return isWithinInterval(date, { start: range[0], end: range[1] });
}

function isWithinRanges(date, ranges) {
  return ranges.some(range => isWithinRange(date, range));
}



var moods = {
  'Great': '#FF0000',
  'Good': 'FF8F00',
  'Okay': 'FBFF00',
  'Sad': 'AEFF00',
  'VerySad': '03D015'
};

const mood = 'Sad'
const today = new Date();

const datesToAddClassTo = [];

function tileClassName({ date, view }) {
  // Add class to tiles in month view only
  if (view === 'month') {
    // Check if a date React-Calendar wants to check is on the list of dates to add class to
    if (datesToAddClassTo.find(dDate => isSameDay(dDate, date))) {
      return 'myClassName';
    }
  }
}


function App() {
  const [date, setDate] = useState(today);
  

  return (  
    
    <div className='app'>
      <h1 className='text-center'>Spotify Mood Calender</h1>
      <div className='calendar-container'>
        <Calendar 
        onChange={setDate}
        defaultValue={date} 
        tileClassName={tileClassName}/>
      </div>
      <p className='text-center'>
        <span className='bold'>Today's Date:</span>{' '}
        {today.toDateString()}
      </p>
    </div>
  );
}

export default App;



/*class App extends React.Component {
  constructor(props)
  {
    super(props)
    this.state={
      date:new Date(),
      dayColor: "red"
    }
  }

  previouslySelectedDates = []

  /* tileClass = ({date, view}) => {
    if (view == 'month') {
      if (previouslySelectedDates.find(currentDate => currentDate == date)) {
        return 'newClass'
      }
    }
   }*/

  /*onChange = date => {
    this.previouslySelectedDates.add(date)
    this.setState({ date })
  }

  [date, setDate] = useState(new Date());

  onDateChange = (newDate) => {
    setDate(newDate);
    console.log(newDate);
  }


  render()
  {
    return (
      <Calendar
          onChange={onDateChange}
          value={date}
          showNeighboringMonth={false}
          locale={"en-US"}
       />
  );
  }
}

export default App;*/
