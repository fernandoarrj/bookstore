import React from 'react'

import './Bookstore.css'


const renderForm = () => {
    return (
        <div className="form">
            <input />
            <input />
        </div>
    )
}

const renderTable = () => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Pages</th>
                </tr>
            </thead>
        </table>
    )
}

export default props => 
    <div>
        {renderForm()}
        {renderTable()}
    </div>
