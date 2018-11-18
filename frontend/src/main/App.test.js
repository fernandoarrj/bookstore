import React from 'react'
import App from './App'
import { shallow } from 'enzyme'

import '../tests/configureTests'

it('renders without crashing', () => {
    const wrapper = shallow(<App />)
    expect(wrapper.exists()).toEqual(true)
})
