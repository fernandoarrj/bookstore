import React from 'react'

import './App.css'
import Bookstore from '../components/Bookstore/Bookstore'


const books = [{name: 'Book 1', pages: 22}, {name: 'Book 2', pages: 33}]

export default props =>
    <div>
        <Bookstore books={books}/>
    </div>
