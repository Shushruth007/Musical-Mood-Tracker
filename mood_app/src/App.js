import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import moment from 'moment'

import './App.css';

import { differenceInCalendarDays } from 'date-fns';

function isSameDay(a, b) {
  return differenceInCalendarDays(a, b) === 0;
}

const vs = [
  '01-04-2022',
  '07-04-2022'
]

const s = [
  '09-04-2022'
]

const o = [
  '03-04-2022',
  '05-04-2022',
  '06-04-2022'
]

const go = [
  '08-04-2022'
]
const gr = [
  '02-04-2022',
  '04-04-2022',
]


var moods = {
  'Verysad': '#FF2E1D',
  'Sad': '#FF871D',
  'Okay': '#FFE438',
  'Good': '#CCFF0E',
  'Great': '#6DFF0E'
};

 //Change to test the different moods
const today = new Date();

const datesToAddClassTo = [today];




function App() {
  const [date, setDate] = useState(new Date());
  const [mood, setMood] = useState(0);

  function tileClassName({ date, view }) {
    // Add class to tiles in month view only
  
    if(vs.find(x => x===moment(date).format("DD-MM-YYYY"))){
      return  'verysad'
    }
    if(s.find(x => x===moment(date).format("DD-MM-YYYY"))){
      return  'sad'
    }
    if(o.find(x => x===moment(date).format("DD-MM-YYYY"))){
      return  'okay'
    }
    if(go.find(x => x===moment(date).format("DD-MM-YYYY"))){
      return  'good'
    }
    if(gr.find(x => x===moment(date).format("DD-MM-YYYY"))){
      return  'great'
    }
  
    if (datesToAddClassTo.find(dDate => isSameDay(dDate, date))){
      if (mood == 5) {
        return 'verysad';
      }
      else if (mood == 4) {
        return 'sad';
      }
      else if (mood == 3) {
        return 'okay';
      }
      else if (mood == 2) {
        return 'good';
      }
      else if (mood == 1) {
        return 'great';
      }
      else {
        return 'grey';
      }
    }
  
  }
  
  let serverUrl = 'https://05ee-66-75-246-191.ngrok.io';

  function callBackend() {
    fetch(serverUrl)
    .then(res => res.json())
    .then(data => {
        console.log(data.message)
        setMood(data.message)
    })
      
}
  return (  
    
    <div className='app'>
      <h1 className='text-center'>Spotify Mood Calender</h1>
      <div className='calendar-container'>
        <Calendar 
        onChange={setDate} 
        value={date}
        tileClassName={tileClassName}/>
      </div>
      <div className='date'>
        <p className='text-center'>
          <span className='bold'>Today's Date:</span>{' '}
          {today.toDateString()}
        </p>
        </div>
      <div className='start'>
        <button className='start' onClick={callBackend}>Get Started!</button>
      </div>
    </div>
  );
}

export default App;

