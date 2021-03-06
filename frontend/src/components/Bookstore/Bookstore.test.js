import React from 'react'
import { shallow } from 'enzyme'

import Bookstore from './Bookstore'

import '../../tests/configureTests'

describe('/src/components/Bookstore', () => {

    it('renders bookstore without crashing', () => {
        const wrapper = shallow(<Bookstore />)

        expect(wrapper.exists()).toEqual(true)
    })

    it('bookstore has a table with headers name and pages', () => {
        const wrapper = shallow(<Bookstore />)

        expect(wrapper.find('table').length).toBe(1)
        expect(wrapper.find('thead').length).toBe(1)
        expect(wrapper.find('th').length).toBe(2)
        expect(wrapper.find('th').contains('Name', 'Pages')).toEqual(true)

    })

    it('bookstore has a input form for sender new books', () => {
        const wrapper = shallow(<Bookstore />)

        expect(wrapper.find('.form').length).toBe(1)
        expect(wrapper.find('input').length).toBe(2)
    })

    it('should render a rows with name and pages.', () => {
        const books = [{name: 'Book 1', pages: 22}, {name: 'Book 2', pages: 33}]
        const wrapper = shallow(<Bookstore books={books} />)

        expect(wrapper.find('tbody').length).toBe(1)
        expect(wrapper.find('td').length).toBe(4)
    })

})


