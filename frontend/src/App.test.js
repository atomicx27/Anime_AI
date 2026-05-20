import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Anime Agents header', () => {
  render(<App />);
  const headerElements = screen.getAllByText(/Anime Agents/i);
  expect(headerElements.length).toBeGreaterThan(0);
});
