import { useState } from 'react';
import ProductTable from '../components/ProductTable';

const availableQueries = [
  "headphones",
  "smartphones",
  "laptops",
  "tablets",
  "cameras",
  "gaming consoles",
  "smartwatches",
  "wireless earbuds",
  "keyboards",
  "monitors"
];

const Home = () => {
  const [query, setQuery] = useState('headphones');

  const handleChange = (e) => {
    setQuery(e.target.value.toLowerCase());
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-50 to-blue-100 flex flex-col items-center py-10 px-4">
      {/* header */}
      <header className="mb-10">
        <h1 className="text-5xl font-extrabold text-gray-800 text-center">
          Amazon Scraper Dashboard
        </h1>
        <p className="mt-4 text-lg text-gray-600 text-center">
          Browse products scraped directly from Amazon. Select a category below to get started!
        </p>
      </header>

      {/* dropdown selection */}
      <div className="w-full max-w-md">
        <label htmlFor="product-category" className="block text-gray-700 text-sm font-bold mb-2">
          Select Product Category
        </label>
        <div className="relative">
          <select
            id="product-category"
            value={query}
            onChange={handleChange}
            className="block appearance-none w-full bg-white border border-gray-300 hover:border-gray-400 px-4 py-3 pr-8 shadow focus:outline-none focus:shadow-outline transition duration-200 rounded-xl"
          >
            {availableQueries.map((q, index) => (
              <option key={index} value={q}>
                {q.charAt(0).toUpperCase() + q.slice(1)}
              </option>
            ))}
          </select>
          {/* dropdown arrow */}
          <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path d="M5.516 7.548l4.484 4.484 4.484-4.484L16 8.484l-6 6-6-6z" />
            </svg>
          </div>
        </div>
      </div>

      {/* product table */}
      <div className="w-full max-w-7xl mt-10 px-4">
        <ProductTable query={query} />
      </div>
    </div>
  );
};

export default Home;
