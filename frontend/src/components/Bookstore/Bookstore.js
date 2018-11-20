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

const renderRows = (rows) => {
    if (!rows) { return null }

    return (
        rows.map(r => (
            <tr key={r.name}>
                <td>{r.name}</td>
                <td>{r.pages}</td>
            </tr>
            ))
    )
}

const renderTable = (rows) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Pages</th>
                </tr>
            </thead>
            <tbody>
                {renderRows(rows)}
            </tbody>
        </table>
    )
}

export default props => 
    <div>
        {renderForm()}
        {renderTable(props.books)}
    </div>
