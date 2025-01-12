import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

const ProductTable = ({ query }) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch(`/data/${query}.json`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setProducts(data);
        setLoading(false);
      } catch (err) {
        setError(`Failed to load data for query "${query}". Ensure the JSON file exists. Error: ${err.message}`);
        setLoading(false);
      }
    };

    if (query) {
      setLoading(true);
      setError(null);
      fetchProducts();
    }
  }, [query]);

  if (loading) return <p className="text-center text-gray-500">Loading...</p>;
  if (error) return <p className="text-center text-red-500">{error}</p>;

  if (products.length === 0) {
    return <p className="text-center text-gray-700">No products found for &quot;{query}&quot;.</p>;
  }

  return (
    <div className="overflow-x-auto rounded-xl">
      <div className="min-w-full bg-white shadow-lg rounded-lg overflow-hidden">
        <table className="min-w-full leading-normal ">
          <thead >
            <tr >
              <th className="px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Image
              </th>
              <th className="max-w-72 px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Title
              </th>
              <th className="px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider max-w-24">
                Price
              </th>
              <th className="max-w-24 px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Rating
              </th>
              <th className="max-w-32 px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Reviews
              </th>
              <th className="px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider max-w-48">
                Buyers
              </th>
              <th className="px-5 py-3 bg-gray-100 text-center text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Scrape Date
              </th>
            </tr>
          </thead>
          <tbody>
            {products.map((product, index) => (
              <tr
                key={index}
                className={`${
                  index % 2 === 0 ? 'bg-white' : 'bg-gray-50'
                } hover:bg-gray-200 transition duration-300`}
              >
                <td className="px-5 py-5 border-b border-gray-200">
                  <div className="flex items-center">
                    <div className="flex-shrink-0 w-16 h-16">
                      <img
                        src={product.image_url}
                        alt={product.title}
                        className="w-full h-full object-cover rounded"
                        loading="lazy"
                      />
                    </div>
                  </div>
                </td>
                <td className="px-5 py-5 border-b border-gray-200 max-w-80">
                  <div className="text-sm text-gray-900 font-medium">{product.title}</div>
                </td>
                <td className="px-5 py-5 border-b border-gray-200 max-w-24">
                  <span className="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight">
                    <span
                      aria-hidden="true"
                      className="absolute inset-0 bg-green-200 opacity-50 rounded-full"
                    ></span>
                    <span className="relative">{product.price}</span>
                  </span>
                </td>
                <td className="px-5 py-5 border-b border-gray-200 max-w-24">
                  <div className="flex items-center">
                    <span className="ml-4 text-sm text-gray-900">{product.rating}</span>
                    <svg
                      className="w-4 h-4 text-yellow-500"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.286 3.967a1 1 0 00.95.69h4.181c.969 0 1.371 1.24.588 1.81l-3.392 2.463a1 1 0 00-.364 1.118l1.286 3.967c.3.921-.755 1.688-1.54 1.118l-3.392-2.463a1 1 0 00-1.176 0l-3.392 2.463c-.785.57-1.838-.197-1.54-1.118l1.286-3.967a1 1 0 00-.364-1.118L2.98 9.394c-.783-.57-.38-1.81.588-1.81h4.181a1 1 0 00.95-.69l1.286-3.967z" />
                    </svg>
                  </div>
                </td>
                <td className="px-5 py-5 border-b border-gray-200 max-w-32">
                  <span className="relative inline-block px-3 py-1 font-semibold text-blue-900 leading-tight ml-4">
                    <span
                      aria-hidden="true"
                      className="absolute inset-0 bg-blue-200 opacity-50 rounded-full"
                    ></span>
                    <span className="relative">{product.reviews}</span>
                  </span>
                </td>
                <td className="px-5 py-5 border-b border-gray-200 max-w-48">
                  <span className="relative inline-block px-3 py-1 font-semibold text-purple-900 leading-tight">
                    <span
                      aria-hidden="true"
                      className="absolute inset-0 bg-purple-200 opacity-50 rounded-full"
                    ></span>
                    <span className="relative">{product.buyers}</span>
                  </span>
                </td>
                <td className="px-5 py-5 border-b border-gray-200">
                  <span className="text-sm text-gray-900">
                    {new Date(product.scrape_date).toLocaleString()}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
ProductTable.propTypes = {
  query: PropTypes.string.isRequired,
};

export default ProductTable;
