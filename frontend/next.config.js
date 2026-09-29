/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    PORT: process.env.PORT || 3000,
  },
  // Optional: if any customizations needed
}

module.exports = nextConfig