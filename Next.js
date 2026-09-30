### Environment Variables
If your Next.js app requires environment variables, consider setting them in Azure Static Web Apps or embedding during build.

## Notes about cost optimization

- Using Azure Static Web Apps for static hosting optimizes costs within the Azure for Students free tier.
- Serving via nginx container locally is for dev/test only; production uses Azure's CDN.

## Additional info

- The Github Actions workflow is located at `.github/workflows/ci-cd.yml`.
- Dockerfile supports multi-stage build and efficient image size.
- `npm run export` is used to create static HTML export for best scalability.

---

For questions or issues, please contact the DevOps team.